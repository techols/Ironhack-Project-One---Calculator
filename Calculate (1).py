#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

class Solution:
    def calculate(self, s: str) -> int:
        return
# A really simple expression evaluator supporting the
# four basic math functions, parentheses, and variables.

# parser: strings needs to be seperated and evaluated in order to do the mathematical operations manually.
# The methodology is dependent on classes and objects in order to be able store and analyze variable/characters
# more easily.This section also ensures that errors are found. 
class Parser: 
    def __init__(self, string, vars={}): #vars is for var() function
        self.string = string
        self.index = 0
        for var in vars.keys():
            if self.vars.get(var) != None:
                raise Exception("Cannot redefine the value of " + var)
            self.vars[var] = vars[var]
#The following code also creates a function where as we retrieve characters, we skip over whites spaces.   
    def getValue(self):
        value = self.parseExpression()
        self.skipWhitespace()
        if self.hasNext():
            raise Exception(
                "Unexpected character found: '" +
                self.peek() +
                " at index " +
                str(self.index))
        return value
#peek is used to help the program pick the topmost element in a stack.
#Stacks are linear structures that follow the last in, first out (LIFO) method.
#like a stack of plates, in order to get to plate at the bottom, you have to 
# take off the first plate in order to get to others. 
# In this case, we reverse the order of operations in order to deal with certain elements first.
# Therefore we deal with addition/subtraction,then multiplication/division, then parantheses
    def peek(self):
        return self.string[self.index:self.index + 1]
    
    def hasNext(self):
        return self.index < len(self.string)
#Use of regular expression in order to seperate characters     
    def skipWhitespace(self):
        while self.hasNext():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return
    
    def parseExpression(self):
        return self.parseAddition()
 #addition and subtraction   
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
#multiplication and division    
    def parseMultiplication(self):
        values = [self.parseParentheses()]
        while True:
            self.skipWhitespace()
            char = self.peek()
            if char == '*':
                self.index += 1
                values.append(self.parseParentheses())
            elif char == '/':
                div_index = self.index
                self.index += 1
                denominator = self.parseParentheses()
                ## division by zero, return to zero 
                if denominator == 0:
                    return  0
                values.append(1.0 / denominator)
            else:
                break
        value = 1.0
        for factor in values:
            value *= factor
        return value
#function for parantheses     
    def parseParentheses(self):
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
#to define negative negative integers    
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
#The following class 'def parseVariable' is to ensure that integers as well as characters 
#that act as variables. 
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
#to eliminite floats and ensure that results will be integers.     
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
                        "Error " +
                        str(self.index) +
                        ".")
                decimal_found = True
                strValue += '.'
            elif char in '0123456789':
                strValue += char
            else:
                break
            self.index += 1
        
        return float(strValue)
#Evaluation of the expression while launching the parser function        
def calculate(expression, vars={}):
    try:
        p = Parser(expression, vars)
        value = p.getValue()
    except Exception as ex:
        msg = ex.message
        raise Exception(msg)
        
# Return an integer as a value as opposed to a float(number with a decimal)
#if this part of the code is deleted, it creates a float. 
    if int(value) == value:
        return int(value)    

    return value

print(calculate("1 + 2 * 3"))
print(calculate("1 * (2 + 3) - 4"))
print(calculate("4 * (3 + 2) - 1"))
print(calculate("2 * (6 / 3) - 1"))


# In[ ]:




