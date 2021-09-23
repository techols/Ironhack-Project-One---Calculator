#!/usr/bin/env python
# coding: utf-8

# In[1]:


Number = eval ( '5 * 3' )
print(Number)


# - Interesting Link: https://www.programiz.com/python-programming/examples/calculator
#   - notes: this looks too easy 
# - Other link: https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3

# Add two numbers in Python
# 
# https://www.w3schools.com/python/python_howto_add_two_numbers.asp
# 
# Site where there are are several versions of progamming for addition:
# 
# https://pythonguides.com/add-two-numbers-in-python/
# 
# This seems to be the easiest and creates a sum function: 
# 
# https://www.thecrazyprogrammer.com/2017/04/python-program-add-two-numbers.html
# 

# Notes about math in parantheses: http://www.easypythondocs.com/arithmetic.html

# Advice: Needs to recreate PEMDAS operations , advice: parsing out the integers and then do the operators, also make test driven code

# In[32]:


def calculate_sum_for(first,second):
      return int(first) + int(second)
#2
first = "1"
second = "2"
#3
print("The sum for X is",calculate_sum_for(first,second))


# In[33]:


def calculate_subtraction_for(first,second):
      return int(first) - int(second)
#2
first = "2"
second = "1"
#3
print("The sum for X is",calculate_subtraction_for(first,second))


# In[35]:


def calculate_multiply_for(first,second):
      return int(first) * int(second)
#2
first = "5"
second = "3"
#3
print("The multiplication for X is",calculate_multiply_for(first,second))


# In[42]:


def multiply_subtract(first,second,third):
    return int(first) * int(second) - int(third)
#2
first = "4"
second = "3"
third = "1"
#3
print("The multiplication and subtraction of three numbers are",multiply_subtract(first,second,third))


# In[45]:


## a x (b + c) = '1 * (2 + 3)'= 5

def math_parantheses_operation(first,second,third):
    return int(first) * (int(second) + int(third)) 
#2
first = "1"
second = "2"
third = "3"
#3
print("The multiplication and subtraction of three numbers are",math_parantheses_operation(first,second,third))


# Notes from other links:
#     - Parse strings via a 'tree'
#     - use the concepts of tokens to split things up 
#     - Create a dictionary or class of operations
#     
#     
# Links:
# 
# Solution for getting rid of eval:
# 
# https://stackoverflow.com/questions/38860682/evaluating-a-mathematical-expression-without-eval-on-python3
# https://stackoverflow.com/questions/62902096/how-to-evaluate-a-user-input-of-a-string-as-a-math-expression-without-using-eval
# 
# Parsing and printing out more complicated mathematical expressions ( seems more complex than necessary)
# https://nerdparadise.com/programming/parsemathexpr
# 
# Parsing out in 50 or 70 lines
# https://erezsh.wordpress.com/2012/11/18/how-to-write-a-calculator-in-50-python-lines-without-eval/
# https://erezsh.wordpress.com/2013/02/24/how-to-write-a-calculator-in-70-python-lines-by-writing-a-recursive-descent-parser/
# 
# Recursive parser youtube: https://www.youtube.com/watch?v=3ajvrOAydFI
# 
# What is a tree
# https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
# 
# Link from Medium that could be useful:
# https://gist.github.com/qiuyujx/fd285e2a2638978ae08f0b5c3eae54ab
# 
# Other links:
# https://www.youtube.com/watch?v=Lc6VTJafYFw
# https://github.com/gnebehay/parser

# In[ ]:





# https://www.tutorialspoint.com/program-to-add-two-numbers-represented-as-strings-in-python
# 
# https://www.reddit.com/r/learnpython/comments/l1ybvx/making_a_pemdas_calculator/  - this is useful
# 
# https://stackoverflow.com/questions/30841750/adding-strings-as-integers-from-two-lists
# 

# In[36]:


#Calculateur simple a x a - d = '1 x 1 - 4'= -3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def multiply_substract(x, y):
    return x * x - y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Multiply_Substract")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "", num1, "-", num2, "=", multiply_substract(num1, num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break

    else:
        print("Invalid Input")


# In[ ]:





# In[ ]:


print evaluate("(1 + 2) * 3")
print evaluate("-(1 + 2) * 3")
print evaluate("(1-2)/3.0 + 0.0000")
print evaluate("1 + pi / 4")
print evaluate("(a + b) / c", { 'a':1, 'b':2, 'c':3 })
print evaluate("(x + e * 10) / 10", { 'x' : 3 })
print evaluate("1.0 / 3 * 6")
print evaluate("(1 - 1 + -1) * pi")
print evaluate("pi * e")


# Youtube Link: https://www.youtube.com/watch?v=UBavyaQniOI
# 

# - Inverse the recursive pattern
# - Create a grammar to scan the tokens 
# - Create a class of tokens in order to store values from the input 

# In[33]:


# A really simple expression evaluator supporting the
# four basic math functions, parentheses, and variables.

class Parser:
    def __init__(self, string, vars={}):
        self.string = string
        self.index = 0
        for var in vars.keys():
            if self.vars.get(var) != None:
                raise Exception("Cannot redefine the value of " + var)
            self.vars[var] = vars[var]
    
    def getValue(self):
        value = self.parseExpression()
        self.skipWhitespace()
        if self.hasNext():
            raise Exception(
                "Unexpected character found: '" +
                self.peek() +
                "' at index " +
                str(self.index))
        return value
    
    def peek(self):
        return self.string[self.index:self.index + 1]
    
    def hasNext(self):
        return self.index < len(self.string)
    
    def skipWhitespace(self):
        while self.hasNext():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return
    
    def parseExpression(self):
        return self.parseAddition()
    
    def parseAddition(self):
        values = [self.parseMultiplication()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '+':
                self.index += 1
                values.append(self.parseMultiplication())
            elif char == '-':
                self.index += 1
                values.append(-1 * self.parseMultiplication())
            else:
                break
        return sum(values)
    
    def parseMultiplication(self):
        values = [self.parseParenthesis()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '*':
                self.index += 1
                values.append(self.parseParenthesis())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parseParenthesis()
                if denominator == 0:
                    raise Exception(
                        "Division by 0 kills baby whales (occured at index " +
                        str(div_index) +
                        ")")
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value
    
    def parseParenthesis(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '(':
            self.index += 1
            value = self.parseExpression()
            self.skipWhitespace()
            if self.peek() != ')':
                raise Exception(
                    "No closing parenthesis found at character "
                    + str(self.index))
            self.index += 1
            return value
        else:
            return self.parseNegative()
    
    def parseNegative(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '-':
            self.index += 1
            return -1 * self.parseParenthesis()
        else:
            return self.parseValue()
    
    def parseValue(self):
        self.skipWhitespace()
        char = self.peek()
        if char in '0123456789.':
            return self.parseNumber()
        else:
            return self.parseVariable()
    
    def parseVariable(self):
        self.skipWhitespace()
        var = ''
        while self.hasNext():
            char = self.peek()
            if char.lower() in '_abcdefghijklmnopqrstuvwxyz0123456789':
                var += char
                self.index += 1
            else:
                break
        
        value = self.vars.get(var, None)
        if value == None:
            raise Exception(
                "Unrecognized variable: '" +
                var +
                "'")
        return float(value)
    
    def parseNumber(self):
        self.skipWhitespace()
        strValue = ''
        decimal_found = False
        char = ''
        
        while self.hasNext():
            char = self.peek()            
            if char == '.':
                if decimal_found:
                    raise Exception(
                        "Found an extra period in a number at character " +
                        str(self.index) +
                        ". Are you European?")
                decimal_found = True
                strValue += '.'
            elif char in '0123456789':
                strValue += char
            else:
                break
            self.index += 1
        
        if len(strValue) == 0:
            if char == '':
                raise Exception("Unexpected end found")
            else:
                raise Exception(
                    "I was expecting to find a number at character " +
                    str(self.index) +
                    " but instead I found a '" +
                    char +
                    "'. What's up with that?")
    
        return float(strValue)
        
def evaluate(expression, vars={}):
    try:
        p = Parser(expression, vars)
        value = p.getValue()
    except Exception as ex:
        msg = ex.message
        raise Exception(msg)
    
    # Return an integer type if the answer is an integer
    if int(value) == value:
        return int(value)
    
    # If Python made some silly precision error
    # like x.99999999999996, just return x + 1 as an integer
    epsilon = 0.0000000001
    if int(value + epsilon) != int(value):
        return int(value + epsilon)
    elif int(value - epsilon) != int(value):
        return int(value)
    
    return value

print(evaluate("1 + 2 * 3"))
print(evaluate("1 * (2 + 3) - 4"))
print(evaluate("4 * (3 + 2) - 1"))
print(evaluate("2 * (6 / 3) - 1"))


# In[ ]:


print evaluate("(1 + 2) * 3")
print evaluate("-(1 + 2) * 3")
print evaluate("(1-2)/3.0 + 0.0000")
print evaluate("1 + pi / 4")
print evaluate("(a + b) / c", { 'a':1, 'b':2, 'c':3 })
print evaluate("(x + e * 10) / 10", { 'x' : 3 })
print evaluate("1.0 / 3 * 6")
print evaluate("(1 - 1 + -1) * pi")
print evaluate("pi * e")

