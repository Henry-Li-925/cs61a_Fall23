---
Topic: Functions
Class: CS61A
Area: Computer Science
Creation date: 9/10/2023 
Creator: Zhe Li
---
- [1. Building Abstractions with Functions](#1-building-abstractions-with-functions)
  - [1.1. Programming in Python](#11-programming-in-python)
    - [1.1.1.  Statements \& Expressions](#111--statements--expressions)
    - [1.1.2. Functions](#112-functions)
    - [1.1.3. Objects](#113-objects)
    - [1.1.4. Interpreter](#114-interpreter)
    - [1.1.5. Some tips for debugging](#115-some-tips-for-debugging)
  - [1.2. Elements of Programming](#12-elements-of-programming)
    - [1.2.1. Expressions \& Call Expressions](#121-expressions--call-expressions)
    - [1.2.2. Names and the Environment](#122-names-and-the-environment)
    - [1.2.3. Evaluating Nested Expressions](#123-evaluating-nested-expressions)
    - [1.2.4. The Non-Pure Print Function](#124-the-non-pure-print-function)
  - [1.3. Defining New Functions](#13-defining-new-functions)
    - [1.3.1. Environment](#131-environment)
    - [1.3.2. Guide for choosing names](#132-guide-for-choosing-names)
    - [1.3.3. Functions as abstractions](#133-functions-as-abstractions)
  - [1.4. Designing Functions](#14-designing-functions)
    - [1.4.1. Documentation](#141-documentation)
    - [1.4.2. Default Argument Values](#142-default-argument-values)

``
# 1. Building Abstractions with Functions

## 1.1. Programming in Python

### 1.1.1.  Statements & Expressions

Statements primarily describe actions. When the Python interpreter executes a statement, it carries out the corresponding action.

Expression typically describe computations. When Python evaluates an expression, it computes the value of that expression.

The assignment statement

```python
from urllib.request import urlopen
# open the url to import the Shakespeare's excerpts
shakespeare = urlopen('https://www.composingprograms.com/shakespeare.txt')
```

### 1.1.2. Functions

Functions encapsulate logic that manipulates data. `urlopen` is a function. A web address is a piece of data, and the text of Shakespeare's plays is another.

### 1.1.3. Objects

```python
# decode the url into text, then split them into words, and place these words in a set
words = set(shakespeare.read().decode().split())
```

A `set` is a type of object, one that supports set operations like computing intersections and membership.

An object seamlessly bundles together data and then logic that manipulates that data, in a way that manages the complexity of both.

```python
# identify all words that have a length of 6 and are simultaneously a word spelled in reverse.
{w for w in words if len(w)==6 and w[::-1] in words}
```

### 1.1.4. Interpreter

An program that implement the procedure of interpreting code in a predictable way, evaluating compound expressions, is called an interpreter.

### 1.1.5. Some tips for debugging

1. **Test incrementally**: Organize your code into small pieces of modular components that can be tested individually.
2. **Isolate errors**: Upon the individual components you're testing, try to trace the error to the smallest fragment of codes you can before trying to correct it.
3. **Check your assumptions**: Knowing your assumptions at first, such that you can modify codes to optimize what the interpreter would output.
4. **Consult others**

## 1.2. Elements of Programming

Three elements as the mechanisms of programming

1. **primitive expressions and statements**: the building blocks of the language ([expression](#expressions--call-expressions))
2. **means of combination**: compounding elements into complex expressions or statements ([nested expression](#evaluating-nested-expressions))
3. **means of abstraction**: compounding elements to be named and manipulated as units ([binding names](#names-and-the-environment))


### 1.2.1. Expressions & Call Expressions

**Basic mathematical expression**: *infix* notation, where the *operator* appears in between the *operands*
$$
1 + 2\\
2 + 4\\
3 * 5\\
8/4
$$

**Call expression**: applying a function to some arguments.
`max(7.5, 9.5)`, `pow(2, 5)`, `math.sub(5, 2)`, `math.mul(12, 4)`

![call-expression](https://www.composingprograms.com/img/call_expression.png)

Function notation has three principal advantages over the mathematical convention of infix notations:

1. functions may take any arbitrary number of argument without arising ambiguity.
2. function notation extends to a straightforward way to nested expressions.
3. function reduces the complexity of various mathematical notations into universal call expressions.

### 1.2.2. Names and the Environment

Names are binding to values by the process of assignment or import.

**assignment**:

```python
radius = 10
radius
```

**import**:

```python
from math import pi
pi
```

When names are bound to functions, Python prints an identifying description instead.

```python
>>> max
<built-in function max>
```

When executing an assignment statement, Python evaluates the expression to the right of `=` before changing the binding to the name on the left.

```python
>>> x = 2
>>> x = x + 1
>>> x
3
```

We can also assign multiple values to multiple names in a single statement, where names on the left of `=` and expressions on the right of `=` are separated by a commas.

```python
>>> area, circumference = pi * radius * radius, 2 * pi * radius
>>> area
314.1592653589793
>>> circumference
62.83185307179586
```

With multiple statement, *all* expressions to the right of `=` are evaluated before `any` names to the left are bound to those values.
```python 
# swapping values bound to two names by a single line of statement
>>> x, y = 3, 4.5
>>> y, x = x, y
>>> x
4.5
>>> y
3
```

### 1.2.3. Evaluating Nested Expressions

a top-down *expression tree*: Evaluating the full expression at the top requires first evaluating the branches that are its subexpressions.

![hierarchy-of-nested-expressions](https://www.composingprograms.com/img/expression_tree.png)

### 1.2.4. The Non-Pure Print Function

**Pure functions**: Functions have some input and return some output.

![pure func: abs()](https://www.composingprograms.com/img/function_abs.png)

**Non-pure functions**: In addition to returning a value, applying an non-pure function can generate *side effects*, which make some change to the state of the interpreter or computer. A common side effect is to generate additional output beyond the return value. [more to cover in chapter 2]()

![non-pure func: print()](https://www.composingprograms.com/img/function_print.png)
![Example_of_print](/images/Example_of_print.png)

While `print` and `abs` may appear to be similar in these examples, they work in fundamentally different ways. The value that `print` returns is always `None`, a special Python value that represents nothing. The interactive Python interpreter does not automatically print the value `None`. In the case of `print`, the function itself is printing output as a side effect of being called.

A nested expression of calls to `print` highlights the non-pure character of the function.

```python
>>> print(print(1), print(2))
1
2
None None
```

```python
>>> two = print(2)
2
>>> print(two)
None
```

## 1.3. Defining New Functions

Function definition is a more powerful tool of abstraction by which a name can be bound to compound operation, which can be referred to as a unit.

**How to define a function**:

1. `def` statement
2. `return` statement
3. the second line must be indented.

```python
def <name>(<formal parameter>):
    return <return expression>
```

### 1.3.1. Environment

An environment in which an expression is evaluated consists of a sequence of *frames*, depicted as boxes. Each frame contains *bindings*, each of which associates a name with its corresponding value. There is a single *global* frame. Assignment and import statements add entries to the first frame of the current environment.

Names are bound to values, which are distributed across many independent local frames, along with a single global frame that contains shared names. A new local frame is introduced every time a function is called, even if the same function is called twice. All three local frames contain a binding for the name `x`, but that name is bound to different values in different frames. Local frames keep these names separate.

```python
>>> def square(x):
        return mul(x, x)
>>> def square(y):
        return mul(y, y)
```

The choose of function's formal parameters has no effect on the function's behavior. This principle of independence has one of the simplest consequences that the parameter names of a function must remain local to the body of the function.

Another expression of this principle is called *scoping*. We say that the *scope* of a local name is limited to the body of the user-defined function that defines it. When a name is no longer accessible, it is out of scope.

### 1.3.2. Guide for choosing names

[style guide for Python code](https://peps.python.org/pep-0008/)

1. Function names are lowercase, with words separated by underscores. Descriptive names are encouraged.
2. Function names typically evoke operations applied to arguments by the interpreter (e.g., `print`, `add`, `square`) or the name of the quantity that results (e.g., `max`, `abs`, `sum`).
3. Parameter names are lowercase, with words separated by underscores. Single-word names are preferred.
4. Parameter names should evoke the role of the parameter in the function, not just the kind of argument that is allowed.
5. Single letter parameter names are acceptable when their role is obvious, but avoid "l" (lowercase ell), "O" (capital oh), or "I" (capital i) to avoid confusion with numerals.


### 1.3.3. Functions as abstractions

a function definition should be able to suppress details. The users of the function may not have written the function themselves, but may have obtained it from another programmer as a "black box". A programmer should not need to know how the function is implemented in order to use it.

**Aspects of a functional abstractions**:

1. *domain*: the set of arguments the function can take
2. *range*: the set of values the function can return
3. *intent*: the relationship the function computes between inputs and outputs.

For example, defining a `square` function that should have these attributes:

```python
from math import mul
def square(x):
    return mul(x,x)
```

- The *domain* is any single real number.
- The *range* is any non-negative real number.
- The *intent* is that the output is the square of the input.

## 1.4. Designing Functions

Good functions encapsulate the idea of abstractions. Fundamentally, all good functions are way of abstractions that are good at generalization and reducing repeat and redundancy.

1. Each function should have exactly one job. Functions that perform multiple jobs in sequence should be divided into multiple functions.
2. *Don't repeat yourself*. The so-called DRY principle states that multiple fragments of code should not describe redundant logic. Instead, that logic should be implemented once, given a name, and applied multiple times. If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction.
3. Functions should be defined generally. 

These guidelines improve the readability of code, reduce the number of errors, and often minimize the total amount of code written.

### 1.4.1. Documentation

*Docstring*: documentations included to describe a function.

Way of declare: Triple quote `"""docstring"""`

By incurring `help()` function, we can see docstrings that describe the function by explaining its functionality and giving examples.

```python
>>> def pressure(v, t, n):
        """Compute the pressure in pascals of an ideal gas.

        Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```

[Docstring Guidelines](https://peps.python.org/pep-0257/) in Python docs guides developers to maintain consistency across different Python projects.

Another way to increase interpretability is to comment at the end of a line or in single lines. `#`

### 1.4.2. Default Argument Values

Defining default argument values of a function is a way of increase generality.

```python
>> def pressure(v, t, n=6.022e23):
        """Compute the pressure in pascals of an ideal gas.

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas (default: one mole)
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v
```

The `=` symbol in the `def` line is used to set a default value to the formal parameter `n`. Whereas, another `=` existing within the body of function that assigns `k` to `1,38e-23` performs as an assignment symbol rather than defining the default value.

As a guideline, most data values used in a function's body should be expressed as default values to named arguments, so that they are easy to inspect and can be changed by the function caller. Some values that never change, such as the fundamental constant `k`, can be found in the function body or the global frame.
