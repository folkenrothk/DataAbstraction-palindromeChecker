"""Determine whether or not an input string is a palindrome."""

# Reference:
# https://en.wikipedia.org/wiki/Palindrome

def to_chars(word: str) -> str:
    """Changing the string to chars in a string"""
    word = word.lower()
    letters = ''
    for _ in word:
        if _ in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + _
    return letters

def is_palindrome(word:str) -> bool:
    if len(word) <= 1:
        return True
    else: 
        return word[0] == word[-1] and is_palindrome(word[1:-1])

def is_palindrome_recursive(word: str) -> bool:
    return is_palindrome(to_chars(word))

def is_palindrome_reverse(word: str) -> bool:
    to_chars(word)
    temp = word[::-1]
    return temp == word
