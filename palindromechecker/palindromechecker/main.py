"""Perform palindrome checking in CLI."""

# import all of the required packages and modules
from enum import Enum

import typer

from rich.console import Console

from palindromechecker import palindrome
from palindromechecker import util

# create the command-line interface object with typer
cli = typer.Typer()

# define a PalindromeCheckingApproach enumeration with these options:
# --> "recursive": use the recursive approach described on page 129
# --> "reverse": use the recursive approach described on page 164


class PalindromeCheckingApproach(str, Enum):
    """Determine which approach is being called."""

    is_palindrome_recursive = "recursive"
    is_palindrome_reverse = "reverse"


# implement a command-line interface using typer that produces output like those examples included in the remainder of this file
@cli.command()
def palindromechecker(
    word: str = typer.Option(...),
    approach: PalindromeCheckingApproach = PalindromeCheckingApproach.is_palindrome_reverse,
) -> None:
    """Use a method to determine if an input string is a palindrome or not."""
    console = Console()
    # poetry run palindromechecker --help
    # Usage: palindromechecker [OPTIONS]
    #
    #   Use a method to determine if an input string is a palindrome or not.
    #
    # Options:
    #   --word TEXT                     [required]
    #   --approach [recursive|reverse]  [default: reverse]
    #   --install-completion            Install completion for the current
    #                                   shell.
    #   --show-completion               Show completion for the current shell,
    #                                   to copy it or customize the
    #                                   installation.
    #
    #   --help                          Show this message and exit.

    # Output of: poetry run palindromechecker --word {word} --approach {approach}
    console.print(
        f":sparkles: Awesome, using the {approach} approach for palindrome checking!"
    )
    console.print()
    console.print(
        f':bookmark: Going to check to see if the word "{word}" is a palindrome!'
    )
    if approach.value == PalindromeCheckingApproach.is_palindrome_recursive:
        result = palindrome.is_palindrome_recursive(word)
        result = util.get_human_readable_boolean(result)
    elif approach.value == PalindromeCheckingApproach.is_palindrome_reverse:
        result = palindrome.is_palindrome_reverse(word)
        result = util.get_human_readable_boolean(result)
    console.print()
    console.print(":grinning_squinting_face: Is this word a palindrome? " + str(result))
