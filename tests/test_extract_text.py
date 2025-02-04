import unittest
import sys
import os
from pathlib import Path

# Add the porject root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from pdf_parse.extract_text import extract_text_from_pdf

class TestExtractText(unittest.TestCase):
    def setUp(self):
        # Move up one directory from tests to the project root.
        base_path = Path(__file__).resolve().parent.parent
        # Define the attribute sample_pdf correctly.
        self.sample_pdf = base_path / "pdf-parse-pickup" / "Sample-Completed-SBC.pdf"

    def test_extract_text_returns_string(self):
        extracted = extract_text_from_pdf(str(self.sample_pdf))
        self.assertIsInstance(extracted, str)
        self.assertTrue(len(extracted) > 0, "Extracted text should not be empty.")

    def test_extract_text_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            extract_text_from_pdf("nonexistent_file.pdf")

if __name__ == "__main__":
    unittest.main()