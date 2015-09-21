#OPERATORS
def isTypeOperator(char):
    return char == "PLUS" or char == "MINUS" or char == "TIMES" or char == "DIVIDE" or char == "EXP" or char == "MOD"

def isOperator(char):
    return char == "+" or char == "-" or char == "*" or char == "/" or char == "^" or char == "mod"

def howManyOperator(char):
    return char.count("+") + char.count("-") + char.count("*") + char.count("/") + char.count("^") + char.count("mod")

def mapOperatorToToken(char):
    if char == "+":
        return "PLUS"

    if char == "-":
        return "MINUS"

    if char == "*":
        return "TIMES"

    if char == "/":
        return "DIVIDE"

    if char == "^":
        return "EXP"

    if char == "mod":
        return "MOD"

def performOperation(operatorType, leftValue, rightValue):
    if operatorType == "PLUS":
        return leftValue + rightValue    
    if operatorType == "MINUS": 
        return leftValue - rightValue
    if operatorType == "TIMES": 
        return leftValue * rightValue
    if operatorType == "DIVIDE": 
        return leftValue / rightValue
    if operatorType == "EXP": 
        return leftValue ** rightValue
    if operatorType == "MOD":
        return leftValue % rightValue
