from run import *

def comparison(_text):
    #first figure out if we're dealing with numbers...
    #with numbers, do what's below
    #with string, compare directly (equal or not)
    #with boolean, compare directly (equal or not)
    #with boolean, if no comparison, just return that..
    #evaluate2

    #EVALUATE EXPRESSIONS.....
    if ">" in _text:
        #split string from this and compare
        result1, result2 = calculateTwoExpressions(_text.split(">"))

        if result1 > result2:
            return "true"
        else:
            return "false"

    elif "<" in _text:
        result1, result2 = calculateTwoExpressions(_text.split("<"))

        if result1 < result2:
            return "true"
        else:
            return "false"

    #This might apply for string or boolean too
    elif "==" in _text:
        _split = _text.split("==")
        if _split[0] == _split[1]:
            return "true"

        else:
            result1, result2 = calculateTwoExpressions(_text.split("=="))

            if result1 == result2:
                return "true"
            else:
                return "false"

    elif "!=" in _text:
        _split = _text.split("!=")
        if _split[0] != _split[1]:
            return "true"
        else:
            result1, result2 = calculateTwoExpressions(_text.split("!="))

            if result1 != result2:
                return "true"
            else:
                return "false"
    #END EVALUATING EXPRESSIONS

    #See if it is a plain boolean
    elif _text == "true":
        return "true"
    elif _text == "false":
        return "false"

    else:
        printError("Failed to evaluate condition: " + _text)
        return "Failed to check condition. Comparison is not vaild"

def calculateTwoExpressions(_expressions):
    from run import Interpreter
    interpreter1 = Interpreter(_expressions[0])
    result1 = interpreter1.expr()
    interpreter2 = Interpreter(_expressions[1])
    result2 = interpreter2.expr()

    return result1, result2

def isTypeComparison(char):
    return char == "GREATER" or char == "LESS" or char == "EQUAL" or char == "NOT EQUAL"

def isComparison(char):
    return char == ">" or char == "<" or char == "==" or char == "!="

def containsComparison(char):
    return ">" in char or "<" in char or "==" in char or "!=" in char

def howManyComparison(char):
    return char.count(">") + char.count("<") + char.count("==") + char.count("!=")

def howManySet(string):
    #look at characters next to =
    n = 0
    finalCount = 0
    containsNot = False

    #3 != 2 should be 0
    #3 == 2 should be 0
    #3 = 2 should be 0
    #3 === should be 0
    #3 !== should be 0
    #3 =!= should be 0

    for c in string:
        if c == "!" and n == 1:
            containsNot = True
            n = 0
        elif c == "!":
            containsNot = True
        elif c == "=" and containsNot:
            containsNot = False
        elif c == "=":
            n += 1
        elif n == 1:
            finalCount += 1
            n = 0

    return finalCount