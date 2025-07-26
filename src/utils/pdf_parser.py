"""PDF parsing functionality for liturgical documents."""

from typing import List
import PyPDF2
from loguru import logger

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract all text from PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        logger.error(f"Error extracting text from PDF: {e}")
        return ""


def parse_liturgical_content(text: str) -> List[str]:
    """Parse liturgical content from text."""
    # TODO: Implement parsing logic
    return []


if __name__ == "__main__":
    all_text = extract_text_from_pdf("data/jpkirja.pdf")
    word_count = 0
    for word in all_text.split():
        if word == "Jeesus":
            word_count += 1
    logger.info(f"Sana 'Jeesus' esiintyy {word_count} kertaa")

