# Palindrome Checking

## Kate Folkenroth

## Program Output

### Use four fenced code blocks to provide output from four different runs of `palindromechecker` with different inputs

- **Recursive:**
  - *Input `level` is a palindrome*
  `poetry run palindromechecker --word level --approach recursive`
  
  ```
  ✨ Awesome, using the recursive approach for palindrome checking!

  🔖 Going to check to see if the word "level" is a palindrome!

  😆 Is this word a palindrome? Yes, it is!
  ```

  - *Input `hello` is not a palindrome*
  `poetry run palindromechecker --word hello --approach recursive`

  ```
  ✨ Awesome, using the recursive approach for palindrome checking!

  🔖 Going to check to see if the word "hello" is a palindrome!

  😆 Is this word a palindrome? No, it is not!
  ```

- **Reverse:**
  - *Input `level` is a palindrome*
  `poetry run palindromechecker --word level --approach reverse`

  ```
  ✨ Awesome, using the reverse approach for palindrome checking!

  🔖 Going to check to see if the word "level" is a palindrome!

  😆 Is this word a palindrome? Yes, it is!
  ```

  - *Input `hello` is not a palindrome*
  `poetry run palindromechecker --word hello --approach reverse`

  ```
  ✨ Awesome, using the reverse approach for palindrome checking!

  🔖 Going to check to see if the word "hello" is a palindrome!

  😆 Is this word a palindrome? No, it is not!
  ```

### What is the output from running the test suite with test coverage monitoring?

`poetry run task coverage`

```
C:\Users\Katw\AppData\Local\pypoetry\Cache\virtualenvs\palindromechecker-2wf1vVVw-py3.9\lib\site-packages\coverage\inorout.py:471: CoverageWarning: --include is ignored because --source is set (include-ignored)
  self.warn("--include is ignored because --source is set", slug="include-ignored")
======================================================= test session starts =======================================================
platform win32 -- Python 3.9.6, pytest-5.4.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Users\Katw\OneDrive\Documents\Allegheny\Junior Junior\Fall 21\cmpsc\repos\labs\computer-science-101-fall-2021-ee-palindrome-checking-folkenrothk\palindromechecker
plugins: cov-3.0.0
collected 10 items

tests\test_main.py ....
tests\test_palindrome.py ....
tests\test_util.py ..

----------- coverage: platform win32, python 3.9.6-final-0 -----------
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
palindromechecker\__init__.py         1      0   100%
palindromechecker\main.py            22      0   100%
palindromechecker\palindrome.py      17      0   100%
palindromechecker\util.py             5      0   100%
---------------------------------------------------------------
TOTAL                                45      0   100%


======================================================= 10 passed in 1.08s ======================================================== 
```

## Source Code

### Describe in detail how the completed source code works

#### An example of a test case for the command-line interface of the `palindromechecker`

```
def test_palindromechecker_recursive_is_palindrome():
    """Ensure that the command-line interface works for recursive approach."""
    result = runner.invoke(
        cli, ["--word", "civic", "--approach", "recursive"]
    )
    assert result.exit_code == 0
    assert "recursive" in result.stdout
    assert "reverse" not in result.stdout
    assert "Yes, it is!" in result.stdout
    assert "civic" in result.stdout
```

TODO: Write at least one paragraph to explain the request source code

#### An example of a test case for the `util` module of the `palindromechecker`

```
def test_human_readable_boolean_true():
    """Ensure that a human-readable true boolean works correctly."""
    true_value = True
    true_value_human_readable = util.get_human_readable_boolean(true_value)
    assert true_value_human_readable == "Yes, it is!"
```
TODO: Write at least one paragraph to explain the request source code

#### An example of a test case for the `palindrome` module of the `palindromechecker`

```
def test_short_palindrome_word_recursive():
    """Ensure that a short word of "civic" works correctly."""
    word = "civic"
    result = palindrome.is_palindrome_recursive(word)
    assert result is True
```
TODO: Write at least one paragraph to explain the request source code

## Professional Development

### Think of an appropriate activity that you associate with play. Make a list of the characteristics of that activity that make it seem playful. Are software testing and debugging also playful activities with the same characteristics? Why or why not?

TODO: Provide a two-paragraph response that answers this question in your own words.

### What was the greatest challenge that you faced when completing this assignment?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.

### Leveraging your response to the previous question, how did you overcome the challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.
TODO: Provide a response to this question that is different from any previous answers.
