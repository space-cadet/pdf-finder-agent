import requests
from bs4 import BeautifulSoup
import re
import os
import logging
from urllib.parse import urljoin

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_doi(url):
    """
    Extract DOI from a given URL or string.
    
    Args:
        url (str): The URL or string containing the DOI.
    
    Returns:
        str: The extracted DOI or None if not found.
    """
    doi_pattern = r'10\.\d{4,9}\/[-._;()\/:A-Za-z0-9]+'
    match = re.search(doi_pattern, url)
    return match.group(0) if match else None

def search_doi_by_title(title):
    """
    Search for a DOI using the paper title via the CrossRef API.
    
    Args:
        title (str): The title of the paper.
    
    Returns:
        str: The found DOI or None if not found.
    """
    try:
        logging.info(f"Searching DOI for title: {title}")
        url = "https://api.crossref.org/works"
        params = {"query.title": title, "rows": 1}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        items = data.get("message", {}).get("items", [])
        if items:
            doi = items[0].get("DOI")
            logging.info(f"Found DOI for title '{title}': {doi}")
            return doi
        else:
            logging.warning(f"No DOI found for title: {title}")
            return None
    except requests.RequestException as e:
        logging.error(f"Failed to search DOI by title: {e}")
        return None

def build_scihub_url(doi):
    """
    Build the Sci-Hub URL for a given DOI.
    
    Args:
        doi (str): The DOI of the paper.
    
    Returns:
        str: The Sci-Hub URL.
    """
    scihub_url = f"https://sci-hub.se/{doi}"
    logging.info(f"Built Sci-Hub URL: {scihub_url}")
    return scihub_url

def get_pdf_url(scihub_url):
    """
    Get the PDF URL from the Sci-Hub page.
    
    Args:
        scihub_url (str): The URL of the Sci-Hub page.
    
    Returns:
        str: The URL of the PDF or None if not found.
    """
    try:
        logging.info(f"Requesting Sci-Hub page: {scihub_url}")
        response = requests.get(scihub_url)
        response.raise_for_status()
        logging.info(f"Received response from Sci-Hub: {response.status_code}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        embed = soup.find('embed')
        
        if embed:
            pdf_url = embed.get('src')
            absolute_pdf_url = urljoin(scihub_url, pdf_url)
            logging.info(f"Found PDF URL in embed: {absolute_pdf_url}")
            return absolute_pdf_url
        else:
            logging.warning("No embed found on the Sci-Hub page.")
            logging.debug(f"Sci-Hub page content: {soup.prettify()}")
            return None
    except requests.RequestException as e:
        logging.error(f"Failed to get PDF URL from Sci-Hub: {e}")
        return None

def download_pdf(pdf_url, save_path):
    """
    Download the PDF from the given URL and save it to the specified path.
    
    Args:
        pdf_url (str): The URL of the PDF.
        save_path (str): The path to save the downloaded PDF.
    """
    try:
        logging.info(f"Requesting PDF: {pdf_url}")
        response = requests.get(pdf_url)
        response.raise_for_status()
        logging.info(f"Received response for PDF: {response.status_code}")
        with open(save_path, 'wb') as f:
            f.write(response.content)
        logging.info(f"Downloaded PDF to {save_path}")
    except requests.RequestException as e:
        logging.error(f"Failed to download PDF: {e}")
    except IOError as e:
        logging.error(f"Failed to save PDF: {e}")

def download_papers(paper_list, output_dir):
    """
    Download papers from a list of DOIs or URLs and save them to the specified directory.
    
    Args:
        paper_list (list): A list of DOIs, URLs, or paper titles.
        output_dir (str): The directory to save the downloaded PDFs.
    """
    os.makedirs(output_dir, exist_ok=True)
    for paper in paper_list:
        doi = extract_doi(paper) if 'http' in paper else None
        if not doi:
            doi = extract_doi(paper)
        if not doi:
            logging.info(f"Attempting to search DOI for title: {paper}")
            doi = search_doi_by_title(paper)
        if not doi:
            logging.warning(f"Skipping invalid input: {paper}")
            continue
        save_path = os.path.join(output_dir, f"{doi.replace('/', '_')}.pdf")
        if os.path.exists(save_path):
            logging.info(f"PDF already exists at {save_path}, skipping download.")
            continue
        scihub_url = build_scihub_url(doi)
        pdf_url = get_pdf_url(scihub_url)
        if pdf_url:
            download_pdf(pdf_url, save_path)
        else:
            logging.warning(f"Failed to find PDF for: {doi}")

# Example usage
if __name__ == "__main__":
    papers = [
        "Superspace and the Nature of Quantum Geometrodynamics",
        "On the Extra Current",
        "On Cauchy's Problem in General Relativity - II",
        "Finite-Velocity Diffusion"
    ]
    download_papers(papers, "downloaded_papers")