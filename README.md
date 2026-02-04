# Assignment1-B211-Password Generator
**a) Purpose of the Program:**

The purpose of this program is to generate secure passwords using Python’s built-in standard modules. The program allows users to create either memorable passwords (based on random words and digits) or random passwords (based on randomly selected characters). This assignment is designed to practice using standard Python modules in a real-world scenario while reinforcing core programming concepts such as modular design, user input handling, loops, and file operations.
#
**b) Input**

The program accepts the following inputs from the user:

- Selection of password type:
  - 1 for a memorable password
  - 2 for a random password
- For memorable passwords:
  - Number of words
  - Desired word casing (lowercase, uppercase, or title case)
- For random passwords:
  - Desired password length
  - Whether punctuation should be included
  - Any characters that should be excluded

The program also reads input from a text file (top_english_nouns_lower_100000.txt) containing a list of English words used to generate memorable passwords.
#
**c) Expected Output**

The program outputs a generated password based on the user’s selections.
Each generated password is also saved to a text file along with the date and time it was created.

- Memorable passwords are saved to: Memorable?Generated_Passwords.txt
- Random passwords are saved to: Random/Generated_Passwords.txt

When generating multiple passwords, the program actually confirms succesfull creation and logging of each password.
#
**d) Type of Execution**

This program uses the following execution types:
- Sequential Execution: The program runs from top to bottom, following a logical sequence of steps.

- Conditional Execution: Conditional statements (if, elif, else) are used to determine password type and validate user input.

- Iterative Execution: Loops are used to generate passwords, process word lists, and generate multiple passwords for testing purposes.

- Modular Execution: The program is organized into functions and methods to improve readability and reusability.
#
**e) Possible Improvements**

The possible improvements to this program may include:
- Adding additional password strength checks
- Improving input validation and error handling
- Allowing users to customize password formatting further
- Adding a graphical user interface (GUI)

