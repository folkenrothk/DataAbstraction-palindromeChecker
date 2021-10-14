"""Test Suite to determine if all the palindrome checker is working"""
# Reference:
# https://typer.tiangolo.com/tutorial/testing/

from palindromechecker import main

from typer.testing import CliRunner

runner = CliRunner()

def test_palindromechecker_recursive_is_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    result = runner.invoke(cli, ["--word", "civic", "--approach", "recursive"])
    assert result.exit_code == 0
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    assert "Yes, it is!" in result.stdout
    assert "civic" in result.stdout


def test_palindromechecker_recursive_is_not_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    result = runner.invoke(cli, ["--word", "taylor", "--approach", "recursive"])
    assert result.exit_code == 0
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    assert "No, it is not!" in result.stdout
    assert "taylor" in result.stdout

def test_palindromechecker_reverse_is_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    # TODO: implement this test case using the provided example
    result = runner.invoke(cli, ["--word", "civic", "--approach", "reverse"])
    assert result.exit_code == 0
    assert "recursive" not in result.stdout
    assert "reverse" in result.stdout
    assert "Yes, it is!" in result.stdout
    assert "civic" in result.stdout

def test_palindromechecker_reverse_is_not_palindrome():
    """Ensure that the command-line interface works for reverse approach."""
    result = runner.invoke(cli, ["--word", "taylor", "--approach", "reverse"])
    assert result.exit_code == 0
    assert "recursive" not in result.stdout
    assert "reverse" in result.stdout
    assert "No, it is not!" in result.stdout
    assert "taylor" in result.stdout
