---
title: Introduction to Python for Political Scientists
author: Abhishek Dasgupta
date: 2019-01-15
---

# Welcome

## Communication

- website: https://github.com/abhidg/python-course
- e-mail: abhishek.dasgupta@politics.ox.ac.uk
- mailing list: dpir-python-course@maillist.ox.ac.uk

## Textbook

![textbook cover](automate_cover_medium.png)\


- Automate the Boring Stuff with Python, by Al Swiegart
- <https://automatetheboringstuff.com/> free to see online
- Shall be loosely followed

# Let's start!

## Download and install python

- Visit http://python.org
- On Windows: download Python 3.6 (.msi) installer, click and run.
- On Mac: download Python 3.6 (.dmg) installer, click and run.

## IDLE (Interactive Development Environment)

- Easiest way to start Python coding

~~~python
>>> x = "hello"
>>> y = "world"
>>> print(x + ' ' + y)
~~~

## Run the sample code

This program shows the weekday for a date. Link:

<http://python-course.trenozoic.net/ht2018/day_of_week.py>

Check that it opens in IDLE. Then use F5 to run.

Anything with a `#` in front is a comment. Use them liberally!

# Expressions and Types

## Programming modes

- Two modes: interactive and batch
- We shall start with interactive
- Batch mode for programs (use F5 to run)

## Interactive mode

~~~
Python 3.6.4 (default, Jan  5 2018, 02:13:53) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~

Make sure it is Python 3!

Python 2 and 3 are quite different in many ways.

`>>>` is the prompt for your code, which can be expressions or statements.

## Expressions and Statements

Expressions can be *evaluated* (**left to right**)

Examples:

- 2 + 2
- 1.0 / 3.0
- 4 / 2 / 2
- 'hello' + 'world'

Statements are *instructions* which are executed, expressions are *values*

- a = 2
- def f(x): return x * x

## Variables

Variables are boxes for expressions

- `number = 2`
- `python_is_great = True`
- `standardGreeting = 'hello' + ' world'`
- `another = 5`
- `s = number + another`

Naming:

- Must be one word, beginning with letter
- Only alphanumerics and underscore (_)

## Functions

Functions are like boxes for statements with a **input** (optional)
and **output** (optional)

~~~python
def fahrenheit_to_celsius(F):
    return (F - 32) * 5/9
~~~

Now we can use it in an expression:

~~~python
>>> fahrenheit_to_celsius(32)
0.0
~~~

## print()

print(x) shows the value of an expression.

Really useful in code:

- finding problems
- displaying information to users

Not that useful in interactive mode as IDLE evaluates and
shows values anyway.

## Types

- Constants or literals: numbers, strings, booleans
- Every *expression* in Python has a *type*
- *Generally* only same types can be combined via operations

~~~
>>> type(3)
>>> type(3.0)
>>> type(True)
>>> type(False)
>>> type(1/2)
>>> type(1/0)
~~~

## Type of a statement?

~~~
>>> type(a = 2)
>>> type(def f(x): return x)
~~~

## Strings

- In quotes: 'hi'
- Double quotes also work: "hi", useful for representing single quotes
- Concatenation: 'hi' + ' there'
- newlines: special characters representing end of line: '\n'.

## Numbers

- Operators: `+, -, *, /, **` (in increasing order of precedence)
- Expressions are evaluated left to right.
- 2 * 3 + 4 = 10 (not 14)
- Brackets for precedence (only parentheses)
- So 2 * (3 + 4) = 14

## Numbers as seen by Python

- Two main types: `int` and `float`.
- `int` has no limit (except for RAM), `float` has limits:

~~~
>>> import sys
>>> sys.float_info
...
~~~

## Comparison

- Gives booleans: `True` or `False`
- Equality `==, !=`
- Order `<, >, <=, >=`
- Any two expressions in Python can be compared for equality
- Generally only expressions of the same type can be compared for `<` and `>`.
- numbers != strings

~~~
>>> 2 != '2'
True
~~~

- Floating point equality is not precise

## Logical operations

- `and`, `or`, `not`
- Works as expected:

~~~python
>>> not True
False
>>> not False
True
>>> True and False
False
>>> True and True
True
>>> False or True
True
~~~

# Flow Control

## if statement

~~~python
if condition:
   do this
elif condition: # optional
   do something else
else:
   do that
~~~

## while statement

~~~python
while condition:
   do this
~~~

- `break` breaks out of the loop
- `continue` starts next iteration of loop

# practical

## coding

Let's fix the day of week program!

It should output:

(day) (is a | will be | was a) (day of week)

## reading notes

Read chapters 1 and 2 of ATBS, exercises.
