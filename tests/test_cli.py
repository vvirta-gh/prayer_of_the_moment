"""Tests for CLI functionality."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import pytest
from click.testing import CliRunner
from cli.cli import cli


def test_hello_command_with_name():
    """Test hello command with name parameter."""
    runner = CliRunner()
    result = runner.invoke(cli, ['hello', '--name', 'Valtteri'])
    assert result.exit_code == 0
    assert "Hello, Valtteri!" in result.output


def test_hello_command_prompt():
    """Test hello command with prompt."""
    runner = CliRunner()
    result = runner.invoke(cli, ['hello'], input='Valtteri\n')
    assert result.exit_code == 0
    assert "Hello, Valtteri!" in result.output


def test_test_pdf_command():
    """Test test_pdf command."""
    runner = CliRunner()
    result = runner.invoke(cli, ['test_pdf'])
    assert result.exit_code == 0
    assert "Sana 'Jeesus' esiintyy" in result.output