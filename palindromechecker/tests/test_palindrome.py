"""Test Suite: determine if each palindrome algorithm is working properly"""

# Reference:
# https://docs.pytest.org/en/6.2.x/

from palindromechecker import palindrome


def test_short_palindrome_word_recursive():
    """Ensure that a short word of "civic" works correctly."""
    word = "civic"
    result = palindrome.is_palindrome_recursive(word)
    assert result is True


def test_short_not_palindrome_word_recursive():
    """Ensure that a short word of "taylor" does not work correctly."""
    word = "taylor"
    result = palindrome.is_palindrome_recursive(word)
    assert result is False


def test_short_palindrome_word_reverse():
    """Ensure that a short word of "civic" works correctly."""
    word = "civic"
    result = palindrome.is_palindrome_reverse(word)
    assert result is True


def test_short_not_palindrome_word_reverse():
    """Ensure that a short word of "taylor" does not work correctly."""
    word = "taylor"
    result = palindrome.is_palindrome_reverse(word)
    assert result is False
