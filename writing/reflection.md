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

This test case is for the command-line interface created in the main file. This test is written like a function named test_palindromechecker_recursive_is_palindrome. From the multiline comment, we can tell that this test case is to assurve that the command-line interface works with the recursive approach. It uses the runner invoke to interact with the command-line interface with theinputs of "--word civic --approach recursive. The first assert statement checks to make sure that there is not an error and that it exits with an exit code 0. The rest of the  assertions below check if the result has mention of recursive, civic, and "Yes, it is!" and not reverse. 

#### An example of a test case for the `util` module of the `palindromechecker`

```
def test_human_readable_boolean_true():
    """Ensure that a human-readable true boolean works correctly."""
    true_value = True
    true_value_human_readable = util.get_human_readable_boolean(true_value)
    assert true_value_human_readable == "Yes, it is!"
```
This test case is one from the util test suite. The code starts like degining a function named test_human_readable_boolean. From the multiline comment, we know it assures that the human_readable true boolean works correctly. This test case is set up with Pytest. It has the static input as True. It tests the function get_human_readable_boolean from the util file with the input. It then asserts that the actual value with the expected value of "Yes, it is!".

#### An example of a test case for the `palindrome` module of the `palindromechecker`

```
def test_short_palindrome_word_recursive():
    """Ensure that a short word of "civic" works correctly."""
    word = "civic"
    result = palindrome.is_palindrome_recursive(word)
    assert result is True
```
This test case is one from the palindrome test suite. The code starts like defining a function named test_short_palindrome_word_recursive. From the multiline comment, we know that this test assures that the short palindrome civic is recognized correctly. It assigns "word" to the variable word. This word is then used with the recursive function to test if the function is working. Since this is using Pytest, it uses the input word, the function is_palindrome_recursive, and then asserting that the actual output matches the expected output that we assigned.

## Professional Development

### Think of an appropriate activity that you associate with play. Make a list of the characteristics of that activity that make it seem playful. Are software testing and debugging also playful activities with the same characteristics? Why or why not?

An activity like hide-and-seek is associated with play. Some characteristics that make it playful are the searching and surprise, a level of enjoyment and disassocation from work, and an activity with other people. Software testing and debugging does have some elements of play. Especially compared with hide-and-seek, the searching, surprise, and success characteristics are also seen in testing and debugging. For those who enjoy software testing, they may feel like debugging is not work while other hold a different opinion towards it. Testing and debugging can be solitary or a group activity which isn't a requirement of being playful but,  in my experience of debugging, I enjoy it more when working with collegues to debug programs. Overall, I think that software testing and debuggin can be playful for some people.

### What was the greatest challenge that you faced when completing this assignment?

The biggest challenge with this engineering effort was figuring out where to start. This program had multiple files and a large test suite to structure. There are three files (main, palindrome, util) and then three respective test suites. Lastly, this had barely any code already written. I was excited for the prospect of finishing so much code and building my coding confidence but is daunting to stare at. All of these pieces left choices open and without solid direction. There was many thoughts about what would be most efficient or what would make the most sense to start with. 

### Leveraging your response to the previous question, how did you overcome the challenge?

Fortunately, we were questioned and forced to think through how we wanted to start coding in our lab session. My collegues and I started on the util file and util test cases. since we could model it closely off of other projects we had already completed. From there, we moved to the palindrome.py file and its test suite. We often had the two files open, the code file and its respective test cases. The test cases were very helpful to understand what the functions are suppose to do. Lastly, we moved to the main.py file and its test case. I think was a pretty successful course of action as it made sense for me to complete and I was able to complete it without needing to jump around too much. 
