import unittest
from pdf-agent import extract_doi, search_doi_by_title, build_scihub_url, get_pdf_url, download_pdf

class TestPDFAgent(unittest.TestCase):

    def test_extract_doi(self):
        self.assertEqual(extract_doi("https://doi.org/10.1000/xyz123"), "10.1000/xyz123")
        self.assertIsNone(extract_doi("https://example.com"))

    def test_search_doi_by_title(self):
        # This test requires an actual API call, consider mocking requests for unit tests
        doi = search_doi_by_title("On the Electrodynamics of Moving Bodies")
        self.assertIsNotNone(doi)

    def test_build_scihub_url(self):
        doi = "10.1000/xyz123"
        expected_url = "https://sci-hub.se/10.1000/xyz123"
        self.assertEqual(build_scihub_url(doi), expected_url)

    def test_get_pdf_url(self):
        # This test requires an actual Sci-Hub page, consider mocking requests for unit tests
        scihub_url = "https://sci-hub.se/10.1000/xyz123"
        pdf_url = get_pdf_url(scihub_url)
        self.assertIsNotNone(pdf_url)

    def test_download_pdf(self):
        # This test requires an actual PDF URL, consider mocking requests for unit tests
        pdf_url = "https://example.com/sample.pdf"
        save_path = "sample.pdf"
        download_pdf(pdf_url, save_path)
        self.assertTrue(os.path.exists(save_path))

if __name__ == '__main__':
    unittest.main()