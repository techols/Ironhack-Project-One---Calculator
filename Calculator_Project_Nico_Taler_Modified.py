#!/usr/bin/env python
# coding: utf-8

# ### Code Proposal with Commentary

# In[33]:


# A really simple expression evaluator supporting the
# four basic math functions, parentheses, and variables.

# parser: strings needs to be seperated and evaluated in order to do the mathematical operations manually.
# The methodology is dependent on classes and objects in order to be able store and analyze variables
# more easily. 

class Parser: 
    def __init__(self, string, vars={}): #vars is for var() function
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
# peek is used to help the program pick the topmost element in a stack.
    def peek(self):
        return self.string[self.index:self.index + 1]
    
    def hasNext(self):
        return self.index < len(self.string)
# elimination of the scanning of whitespaces    
    def skipWhitespace(self):
        while self.hasNext():
            if self.peek() in ' \t\n\r':
                self.index += 1
            else:
                return
# Parsing of values and operations    
    def parseExpression(self):
        return self.parseAddition()
# This function looks for addition and subtraction operations     
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
# This function looks for multiplication and division operations    
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
                ##division by zero
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
# This function looks for operations that are nested in paranthesis.  
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
# This function assures that operation can turn up a negative integer in value    
    def parseNegative(self):
        self.skipWhitespace()
        char = self.peek()
        if char == '-':
            self.index += 1
            return -1 * self.parseParenthesis()
        else:
            return self.parseValue()
# defines what types of values can be used with the operations     
    def parseValue(self):
        self.skipWhitespace()
        char = self.peek()
        if char in '0123456789.':
            return self.parseNumber()
        else:
            return self.parseVariable()
#The following class 'def parseVariable' is to ensure that integers 
#as well as characters that act as variables can be calculated.   
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
# If a variable is in the equeation that has been attributed to previous functions, 
# the program will signal an exception  
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


Other equations to test: 


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

