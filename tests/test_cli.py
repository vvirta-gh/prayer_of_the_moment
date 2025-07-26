import pytest
from click.testing import CliRunner
from cli.cli import cli


def test_hello_command_with_name():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello', '--name', 'Valtteri'])
    assert result.exit_code == 0
    assert "Hello, Valtteri!" in result.output


def test_hello_command_prompt():
    runner = CliRunner()
    result = runner.invoke(cli, ['hello'], input='Valtteri\n')
    assert result.exit_code == 0
    assert "Hello, Valtteri!" in result.output 