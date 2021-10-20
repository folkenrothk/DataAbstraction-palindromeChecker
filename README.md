# Palindrome Checking

## Assigned: Thursday, October 14, 2021
## Due: Thursday, October 21, 2021

After cloning this repository to your computer, please take the following steps:

- Follow the instructions on the Proactive Programmers web site for this project
- Use the `cd` command to change into the directory for this repository
- Change into the program directory by typing `cd palindromechecker`
- Install the dependencies for the project by typing `poetry install`
- Run the program with its different configurations by typing:
  - `poetry run palindromechecker --word civic --approach reverse`
  - `poetry run palindromechecker --word civic --approach recursive`
  - `poetry run palindromechecker --word taylor --approach reverse`
  - `poetry run palindromechecker --word taylor --approach recursive`
  - Please note that the program will not work unless you add the required source code
- Make sure that you have implemented a high-coverage (i.e., 100%) test suite for this program!
- Run the test suite for the program by typing:
  - `poetry run task test`: run the test suite without coverage tracking
  - `poetry run task coverage`: run the test suite with coverage tracking
- Confirm that the program is producing the expected output
- Use a `docker run` command for your operating system to run GatorGrader
- Please be aware that performance profiling in a Docker contain may not work as expected
- Provide all of the required responses in the `writing/reflection.md` file
