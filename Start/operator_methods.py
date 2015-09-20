#OPERATORS
def isTypeOperator(char):
    return char == "PLUS" or char == "MINUS" or char == "TIMES" or char == "DIVIDE" or char == "EXP"

def isOperator(char):
    return char == "+" or char == "-" or char == "*" or char == "/" or char == "^"

def howManyOperator(char):
    return char.count("+") + char.count("-") + char.count("*") + char.count("/") + char.count("^")

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