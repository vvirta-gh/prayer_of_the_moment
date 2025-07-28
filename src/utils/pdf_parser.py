"""PDF parsing functionality for liturgical documents."""

from typing import List
import pypdf
from loguru import logger
import pdfplumber


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract all text from PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
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


def testing_pdfplumber(pdf_path: str):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[1]
        print(first_page.chars[0])




def get_sisallys(pdf_path: str) -> str:
    """Etsii ja palauttaa sisällysluettelon PDF:stä."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text and "Sisällys" in text:
                    logger.info(f"Sisällys löytyi sivulta {page_num + 1}")
                    return text
        return None
    except Exception as e:
        logger.error(f"Virhe PDF:n lukemisessa: {e}")
        return None



if __name__ == "__main__":
    # all_text = extract_text_from_pdf("data/jpkirja.pdf")
    # word_count = 0
    # for word in all_text.split():
    #     if word == "Jeesus":
    #         word_count += 1
    # logger.info(f"Sana 'Jeesus' esiintyy {word_count} kertaa")

    sisallys = get_sisallys("data/jpkirja.pdf")
    if sisallys:
        logger.info(f"Sisällys: {sisallys}")
    else:
        logger.error("Sisällys ei löytynyt")