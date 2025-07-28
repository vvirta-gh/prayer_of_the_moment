"""Tests for PDF parser functionality."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from unittest.mock import Mock, patch, mock_open
from utils.pdf_parser import extract_text_from_pdf, parse_liturgical_content


@patch('builtins.open', new_callable=mock_open)
@patch('pypdf.PdfReader')
def test_extract_text_from_pdf_success(mock_pdf_reader, mock_file):
    """Test successful text extraction from PDF."""
    # Arrange
    mock_page1 = Mock()
    mock_page1.extract_text.return_value = "Ensimmäinen sivu"
    mock_page2 = Mock()
    mock_page2.extract_text.return_value = "Toinen sivu"
    
    mock_reader_instance = Mock()
    mock_reader_instance.pages = [mock_page1, mock_page2]
    mock_pdf_reader.return_value = mock_reader_instance

    # Act
    result = extract_text_from_pdf("test.pdf")

    # Assert
    expected_text = "Ensimmäinen sivuToinen sivu"
    assert result == expected_text
    mock_file.assert_called_once_with("test.pdf", 'rb')


@patch('builtins.open', side_effect=FileNotFoundError("File not found"))
def test_extract_text_from_pdf_file_not_found(mock_file):
    """Test handling of missing PDF file."""
    result = extract_text_from_pdf("nonexistent.pdf")
    assert result == ""


@patch('builtins.open', new_callable=mock_open)
@patch('pypdf.PdfReader', side_effect=Exception("PDF is corrupted"))
def test_extract_text_from_pdf_corrupted_file(mock_pdf_reader, mock_file):
    """Test handling of corrupted PDF file."""
    result = extract_text_from_pdf("test.pdf")
    assert result == ""


@patch('builtins.open', new_callable=mock_open)
@patch('pypdf.PdfReader')
def test_extract_text_from_pdf_empty_pages(mock_pdf_reader, mock_file):
    """Test extraction from PDF with empty pages."""
    mock_page = Mock()
    mock_page.extract_text.return_value = ""
    
    mock_reader_instance = Mock()
    mock_reader_instance.pages = [mock_page]
    mock_pdf_reader.return_value = mock_reader_instance

    result = extract_text_from_pdf("test.pdf")
    assert result == ""


@patch('builtins.open', new_callable=mock_open)
@patch('pypdf.PdfReader')
def test_extract_text_from_pdf_special_characters(mock_pdf_reader, mock_file):
    """Test extraction with special characters and Finnish text."""
    special_text = "Ääkköset: äöå ÄÖÅ. Erikoismerkit: @#$%^&*()"
    mock_page = Mock()
    mock_page.extract_text.return_value = special_text
    
    mock_reader_instance = Mock()
    mock_reader_instance.pages = [mock_page]
    mock_pdf_reader.return_value = mock_reader_instance

    result = extract_text_from_pdf("test.pdf")
    assert result == special_text


@patch('builtins.open', new_callable=mock_open)
@patch('pypdf.PdfReader')
def test_extract_text_from_pdf_multiple_pages(mock_pdf_reader, mock_file):
    """Test extraction from multi-page PDF."""
    mock_pages = []
    for i in range(5):
        mock_page = Mock()
        mock_page.extract_text.return_value = f"Sivu {i+1}"
        mock_pages.append(mock_page)
    
    mock_reader_instance = Mock()
    mock_reader_instance.pages = mock_pages
    mock_pdf_reader.return_value = mock_reader_instance

    result = extract_text_from_pdf("test.pdf")
    expected = "Sivu 1Sivu 2Sivu 3Sivu 4Sivu 5"
    assert result == expected


def test_parse_liturgical_content_empty_input():
    """Test parsing liturgical content from empty text."""
    result = parse_liturgical_content("")
    assert result == []


def test_parse_liturgical_content_sample_text():
    """Test parsing liturgical content from sample text."""
    sample_text = "Rukous: Herra Jeesus Kristus, armahda meitä."
    result = parse_liturgical_content(sample_text)
    assert result == []
