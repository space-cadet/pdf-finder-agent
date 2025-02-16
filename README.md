# PDF Finder Agent

This project is designed to find and download PDFs of academic papers using their DOIs, URLs, or titles. It leverages the CrossRef API and Sci-Hub to locate and retrieve the PDFs.

## Features
- Extract DOI from a given URL or string.
- Search for a DOI using the paper title via the CrossRef API.
- Build the Sci-Hub URL for a given DOI.
- Get the PDF URL from the Sci-Hub page.
- Download the PDF from the given URL and save it to the specified path.
- Download papers from a list of DOIs, URLs, or paper titles and save them to the specified directory.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pdf-finder-agent.git
    cd pdf-finder-agent
    ```
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Edit the [pdf-agent.py](http://_vscodecontentref_/0) file to include the list of papers you want to download.
2. Run the script:
    ```sh
    python pdf-agent.py
    ```

## Credits
- **Designer**: Deepak Vaid (dvaid79@gmail.com)
- **Builder**: GitHub Copilot on VSCode using GPT-4o