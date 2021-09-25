# Creating a Calculator in Python

### Evaluating mathematical expressions with the function eval()

Python is a useful tool to evaluate mathmatical expressions thanks to the eval() function. 


```python
Number = eval ( '5 * 3' )
print(Number)
```

    15


### Why not use Eval function?
- it's insecure depending on its use in a program.
    - if your input is insecure, it could affect the security of the program. 
- Can make debugging difficult
- Can make executable actions slow. 
- The function can impeded dynamic execution 
    
Sources: 

https://realpython.com/python-eval-function/

https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html

https://stackoverflow.com/questions/1832940/why-is-using-eval-a-bad-practice#:~:text=The%20point%20of%20all%20this,t%20need%20to%20use%20it.

https://realpython.com/python-eval-function/#understanding-pythons-eval

### First step: Figure out how to recreate operations via customized functions

Mathematical operations cannot be executed when the expression is in string form. Therefore it is necessary to convert into a form that can be executed via **integer** or **float.** The following functions demonstrate how to break up a string with two elements into integers for mathmatical evaluation. There are other methods but we opted for the following method in order to understand the transformation from strings to integes. 

Source:

https://www.thecrazyprogrammer.com/2017/04/python-program-add-two-numbers.html



```python
def calculate_sum_for(first,second):
      return int(first) + int(second)
#2
first = "1"
second = "2"
#3
print("The sum for X is",calculate_sum_for(first,second))
```

    The sum for X is 3



```python
def calculate_subtraction_for(first,second):
      return int(first) - int(second)
#2
first = "2"
second = "1"
#3
print("The sum for X is",calculate_subtraction_for(first,second))
```

    The sum for X is 1



```python
def calculate_multiply_for(first,second):
      return int(first) * int(second)
#2
first = "5"
second = "3"
#3
print("The multiplication for X is",calculate_multiply_for(first,second))
```

    The multiplication for X is 15



```python
def multiply_subtract(first,second,third):
    return int(first) * int(second) - int(third)
#2
first = "4"
second = "3"
third = "1"
#3
print("The multiplication and subtraction of three numbers are",multiply_subtract(first,second,third))
```

    The multiplication and subtraction of three numbers are 11


We also created a function to satisfy paranthese type operations. 


```python
## a x (b + c) = '1 * (2 + 3)'= 5

def math_parantheses_operation(first,second,third):
    return int(first) * (int(second) + int(third)) 
#2
first = "1"
second = "2"
third = "3"
#3
print("The multiplication and subtraction of three numbers are",math_parantheses_operation(first,second,third))
```

    The multiplication and subtraction of three numbers are 5


#### PEMDAS ?
We also discovered that Python has established an order of operations protocol called **PEMDAS** in order for the language to interpret correctly mathmatical rules when it uses mathematical functions such as **eval()**. Another challenge of this project is to re-incorporate these type operations manually into our code. 

Sources: 

http://www.easypythondocs.com/arithmetic.html


### Second Step: Parsing

To parse, means to break down a whole into more understandable parts.

In the case of this project. It is necessary to create a function that allows us to seperate the elements in the string ( numbers and operations) and are interpreted correctly when evaluated manually.

A parser will establish several objectifs:
- convert numbers in strings into integers that can be used in mathematical expressions
- break down PEMDAS operations to interpreted manually. 

Parsers can accomplish this task in several steps:
- Scan the 'tree' for compenents via a Lexer
- These components are then broken down into tokens
- After this step, then the information is parsed

This information can be used to create a dictionary or a class operations in order to classify the tokens as means of storage for input. 

*Sources:*

What is a tree
https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

https://tomassetti.me/parsing-in-python/

https://www.youtube.com/watch?v=3ajvrOAydFI - Series on the use of recursive descent parser in a calculator 

https://www.youtube.com/watch?v=Lc6VTJafYFw - Another video about creating a parser in order to construct a calculator

https://www.youtube.com/watch?v=UBavyaQniOI

https://github.com/gnebehay/parser


#### Other sources: 

Solution for getting rid of eval:

https://stackoverflow.com/questions/38860682/evaluating-a-mathematical-expression-without-eval-on-python3
https://stackoverflow.com/questions/62902096/how-to-evaluate-a-user-input-of-a-string-as-a-math-expression-without-using-eval

**Code Inspiration**

Parsing and printing out more complicated mathematical expression
https://nerdparadise.com/programming/parsemathexpr

Parsing out in 50 or 70 lines
https://erezsh.wordpress.com/2012/11/18/how-to-write-a-calculator-in-50-python-lines-without-eval/
https://erezsh.wordpress.com/2013/02/24/how-to-write-a-calculator-in-70-python-lines-by-writing-a-recursive-descent-parser/

https://www.reddit.com/r/learnpython/comments/l1ybvx/making_a_pemdas_calculator/ 


```python

```
