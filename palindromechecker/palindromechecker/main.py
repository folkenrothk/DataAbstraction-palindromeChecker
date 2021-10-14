"""Perform palindrome checking in CLI."""

# import all of the required packages and modules
from enum import Enum

import typer

from rich.console import Console

from palindromechecker import util
from palindromechecker import palindrome

# create the command-line interface object with typer
cli = typer.Typer()

# define a PalindromeCheckingApproach enumeration with these options:
# --> "recursive": use the recursive approach described on page 129
# --> "reverse": use the recursive approach described on page 164

class PalindromeCheckingApproach(str, Enum):

    is_palindrome_recursive = "recursive"
    is_palindrome_reverse = "reverse"


# implement a command-line interface using typer that produces output like those examples included in the remainder of this file
@cli.command()
def palindromechecker(
    help: bool = typer.Option(False),
    word: str = typer.Option(...),
    approach: PalindromeCheckingApproach = PalindromeCheckingApproach.is_palindrome_recursive,
) -> None:
    """Determine if the word is a palindrome"""
    console = Console()
    
    # poetry run palindromechecker --help
    if help is True:
        console.print()
# Usage: palindromechecker [OPTIONS]
#
#   Use a method to determine if an input string is a palindrome or not.
#
# Options:
#   --word TEXT                     [required]
#   --approach [recursive|reverse]  [default: reverse]
#   --install-completion            Install completion for the current
#                                   shell.
#
#   --show-completion               Show completion for the current shell,
#                                   to copy it or customize the
#                                   installation.
#
#   --help                          Show this message and exit.
    
    # poetry run palindromechecker --word civic --approach recursive
    elif help is not True:
        console.print(f":sparkles: Awesome, using the {approach} approach for palindrome checking!")
        console.print()
        word = #TODO
        console.print(f":bookmark: Going to check to see if the word {word} is a palindrome!")
# ✨ Awesome, using the recursive approach for palindrome checking!

# 🔖 Going to check to see if the word "civic" is a palindrome!

# 😆 Is this word a palindrome? Yes, it is!
