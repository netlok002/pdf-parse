# PDF Extraction POC

This repository contains a proof-of-concept (POC) project that demonstrates how to extract text from PDF files using Python. The goal of this project is to build a foundation for parsing PDF content, which will eventually be fed to a language model for structured data extraction.

## Project Overview

In this initial iteration, the project:
- Extracts text from PDF files using the `pdfplumber` library.
- Uses relative paths to access PDF files stored in the `pdf-parse-pickup` folder.
- Prints the extracted text to the console and saves it to a text file.

This POC serves as a starting point for a larger workflow that will include further parsing, data obfuscation, and structured CSV output.
