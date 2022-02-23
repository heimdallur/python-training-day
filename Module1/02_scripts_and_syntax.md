# Python Syntax

While this is technically not a programming feature, it’s still crucial to know the current versions of Python as over time important changes to how python is written have occured.

**Example**<br>
Printing a string in Python 2.7<br>
`print "Hello, World!"`

Printing a string in Python 3 and upwards<br>
`print("Hello, World!")`

We also have smaller changes that don't necessarily cause code to nstop working, but should be adhered to if you are creating production quality code. One of the biggest examples of this is [PEP (Python Enterprise Proposal)](https://www.python.org/dev/peps/).<br>

Writing code with proper logic is a key factor of programming, but many other important factors can affect the code's quality. The developer's coding style makes the code much more reliable, and every developer should keep this in mind when developing their code.

Adaptive a nice coding style makes the code more readable. The code becomes easy for other developers and will make your own and other peoples life easier when revisiting code that hasen't been worked with at for a while.

PEP 8 is a document that provides various guidelines to write readable code in Python. PEP 8 describes how the developer can write beautiful code and believe me when I say that developers are always impressed by clean, clear and well written code.

## Common Syntax Errors<hr>

### Indentation

Indentation is strict in python and failing to be at the correct indentation level can cause your code to behave unexpectedly or throw the following error:<br>

    `IndentationError: expected an indented block`
<br>
When indenting in python you must be consitent in your use of `tabs` or `spaces` mixing them will result in the follow error:<br>

    `TabError: Inconsistent Use of Tabs and Spaces in Indentation`

Missing colons on functions is also common when coding when defining a conditional statement of defining a function.

***Example:***

    `if 'ABC' == 'ABC'
        print('They are equal')`

This will throw:

    `SyntaxError: invalid syntax`

as the if line should be

    `if 'ABC' == 'ABC':`

