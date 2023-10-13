---
Topic: Control
Class: CS61A
Area: Computer Science
Creation date: 9/12/2023 
Creator: Zhe Li
---
- [1. Control](#1-control)
  - [1.1. Statement](#11-statement)
  - [1.2. Compound Statements](#12-compound-statements)
  - [1.3. Local Assignment](#13-local-assignment)
  - [1.4. Conditional Statements](#14-conditional-statements)
    - [1.4.1. Short-circuiting with Boolean Operators](#141-short-circuiting-with-boolean-operators)
  - [1.5. Iteration](#15-iteration)
  - [1.6. Testing](#16-testing)


## 1. Control

*Control Statement*: They are statements that control the flow of a program's execution based on the results of logical comparisons. As a control statement, it has no value but determines what the interpreter should do next.

### 1.1. Statement

The characteristics of statement:

1. Does not have values, thus cannot be evaluated but executed.
2. Describes some change to the interpreter state, and executing a statement applies that change.

The difference between expression and statement:

In terms of executing evaluation, expression can make do however at the cost of discarding what has been evaluated. 
For example:

```python
>>> def square(x):
        mul(x, x) # Watch out! This call doesn't return a value.
```


In this case, the `square` function has been correctly stated with a intention to square an input variable, however, the value evaluated by the `mul()` in the body of the function does not be stored rather than discarded. To ensure that value is stored within the frame, we have to call `return` statement:

```python
>>> def square(x):
        return mul(x, x)
```

Some exceptions that make sense to have a function whose body is an expression, is when a non-pure function like `print` is called.

```python
>>> def print_square(x):
        print(square(x))
```

Much of the interesting work of computation comes from evaluating expressions. Statements govern the relationship among different expressions in a program and what happens to their results.

### 1.2. Compound Statements

Compound statements typically span multiple lines and start with a one-line header ending in a colon, which identifies the type of statement. Together, a header and an indented suite of statements is called a *clause*. A compound statement consists of one or more clauses:

```python
<header>:
    <statement>
    <statement>
    ...
<separating header>:
    <statement>
    <statement>
    ...
...
```

- Simple statement: Expressions, `return` statements, and assignment `=` statements
- Compound statement: `def`, `if` statements. The suite that follows these statements defines the function body.

The sequence of multi-line program execution:
    To execute a sequence of statements, execute the first statement. If that statement does not redirect control, then proceed to execute the rest of the sequence of statements, if any remain.

### 1.3. Local Assignment

Whenever a user-defined function is applied, the sequence of clauses in the suite of its definition is executed in a *local environment* - an environment starting with a local frame created by calling that function.

Assignment statements within the body of a function assign values to variables stored in the local environment. When the sequence encounters a `return` statement, the control flow is redirected and returns a value of the function being applied. Rather than being stored within the local frame as those assignments, this value is the outcome that delivered by this function to the global frame, and thus exists beyond the function's scope.

![Local assignment](image/../images/Local%20Assignments.png)


### 1.4. Conditional Statements

*Conditional statements*: A conditional statement in Python consists of a series of headers and suites: a required `if` clause, an optional sequence of `elif` clauses, and finally an optional `else` clause:

```python
if <expression>:
    <suite>
elif <expression>:
    <suite>
else:
    <suite>
```

When executing a conditional statement, each clause is considered in order. The computational process of executing a conditional clause follows.

1. Evaluate the header's expression.
2. If it is a true value, execute the suite. Then, skip over all subsequent clauses in the conditional statement.

If the `else` clause is reached (which only happens if all `if` and `elif` expressions evaluate to false values), its suite is executed.

#### 1.4.1. Short-circuiting with Boolean Operators

> Values in types other than boolean that are equivalent to `False`:
> 0, `None`

The logical expressions in Python are evaluated through a procedure called *short-circuiting*, which sometimes reduces the steps to reach the answer by exploiting the fact that the truth value of a logical expression can sometimes be determined without evaluating all of its subexpressions.

1. To evaluate the expression `<left> and <right>`
   1. Evaluate the subexpression `<left>`.
   2. If the result is a **false** value v, then the expression evaluates to v.
   3. Otherwise, the expression evaluates to the value of the subexpression `<right>`.

2. To evaluate the expression `<left> or <right>`
   1. Evaluate the subexpression `<left>`.
   2. If the result is a **true** value v, then the expression evaluates to v.
   3. Otherwise, the expression evaluates to the value of the subexpression `<right>`.

3. To evaluate the expression `not <exp>`
   1. Evaluate `<exp>`; The value is `True` if the result is a false value, and `False` otherwise.

Some examples

```python
>>> True and 13
13

>>> -1 or 5
-1

>>> print(3) or ''
3 # it calls `print(3)` that doesn't 'return' but rather 'display' 3.
'' # The value 'print(3)' returns is actually `None`, thus makes it evaluate to 'False' and prompts the expression evaluate to the value of '' (right one)

>>> 3 or ''
3

>>> def f(x):
...     if x == 0:
...         return "I am zero!"
...     elif x > 0:
...         return "Positive!"
...     else:
...         return ""

>>> 0 or f(1)
"Positive!"

>>> f(0) or f(-1)
"I am zero!"

>>> f(0) and f(-1)
""
```

### 1.5. Iteration

An example function returns the a Fibonacci number at the `n` index.

```python
def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    pred, curr = 0, 1   # Fibonacci numbers 1 and 2
    k = 2               # Which Fib number is curr?
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr
result = fib(8)
```

Remember the sequence of binding and evaluation on the both side of a `=`:
    All of the expressions to the right of `=` are evaluated before any rebinding takes place.

That is to say, in the case of `pred, curr = curr, pred + curr`, the values to the right of `=` are evaluated at first, then names to the left of `=` would be rebound to the values to the right for the next iteration.

`while` statement

```python
while <expression>:
    <suite>
```

To execute a `while` clause:

1. Evaluate the header's expression.
2. If it is a true value, execute the suite, then return to step 1.
In step 2, the entire suite of the while clause is executed before the header expression is evaluated again.

In order to prevent the suite of a `while` clause from being executed indefinitely, the suite should always change some binding in each pass.

### 1.6. Testing

```
Exhaustive unit testing is a hallmark of good program design.
```

*Testing* is a process of verification that checks whether the function's behavior matches expectation. It is implemented by *test*, which typically take the form of another function that contains one or more sample calls to the function being tested. The returned value is then verified against an expected result.

**Assertions**: `assert` statements used to verify expectations. An `assert` statement has an expression in a boolean context, followed by a quoted line of text that will be displayed if the expression evaluates to a false values.

```python
def fib_text():
    assert fib(2) == 1, 'The 2nd Fibonacci number should be 1' #if the boolean value before the comma returns False, then the text behind prompts out.
    assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number, which should be 12586269025' 
```

Example

```python
def area_square(x):
    assert x > 0, "a length must be positive" #use `assert` statement to avoid unreasonable output.
    return x * x

>>> area_square(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in area_square
AssertionError: a length must be positive
```

When writing Python in files, rather than directly into the interpreter, tests are typically written in the same file or a neighboring file with the suffix `_test.py`.

**Doctests**: another way of testing by directly coding the test in the docstring of a function. By this method, the first line of a docstring should contain a one-line description of the function, followed by a blank line. A detailed description of arguments and behavior may follow. In addition, the docstring may include a sample interactive session that calls the function:

```python
def sum_naturals(n):
    """Return the sum of the first n natural numbers.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total, k = 0, 1
    while k <= 0:
        total, k = total + k, k + 1
    return total
```

Then, the interaction can be verified via the `doctest` module.

```python
>>> from doctest import testmod
>>> testmod()
TestResults(failed=0, attempted=2)
```

To verify the doctest interactions for only a single function, we use a `doctest` function called `run_docstring_examples`. This function is a bit complicated to call. Its first argument is the function to test. The second should always be the result of the expression `globals()`, a built-in function that returns the global environment. The third argument is `True` to indicate that we would like "verbose" output: a catalog of all tests run.

```python
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sun_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```

When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:

`python3 -m doctest <python_source_file>`



