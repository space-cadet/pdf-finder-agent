import requests
from bs4 import BeautifulSoup
import re
import os

def extract_doi(url):
    doi_pattern = r'10\.\d{4,9}\/[-._;()\/:A-Za-z0-9]+'
    match = re.search(doi_pattern, url)
    return match.group(0) if match else None

def build_scihub_url(doi):
    return f"https://sci-hub.se/{doi}"

def get_pdf_url(scihub_url):
    response = requests.get(scihub_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    iframe = soup.find('iframe')
    return iframe['src'] if iframe else None

def download_pdf(pdf_url, save_path):
    response = requests.get(pdf_url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

def download_papers(paper_list, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for paper in paper_list:
        doi = extract_doi(paper) if 'http' in paper else paper
        if not doi:
            print(f"Skipping invalid input: {paper}")
            continue
        scihub_url = build_scihub_url(doi)
        pdf_url = get_pdf_url(scihub_url)
        if pdf_url:
            download_pdf(pdf_url, f"{output_dir}/{doi.replace('/', '_')}.pdf")
            print(f"Downloaded: {doi}")
        else:
            print(f"Failed to find PDF for: {doi}")

# Example usage
papers = [
    "10.1038/nature12373",
    "https://doi.org/10.1016/j.cell.2020.01.001",
    "Deep learning for molecular design"
]
download_papers(papers, "downloaded_papers")