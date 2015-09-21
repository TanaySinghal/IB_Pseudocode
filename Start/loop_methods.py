from run import *

loopSessions = []
#INFORMATION METHODS
def isLoop(_text):
    if _text[:4] == "loop":
        return True

    return False

def loopType(_text):
    if "from" in _text and "to" in _text:
        return "for"
    if "while" in _text:
        return "while"
    printError("Could not recognize loop type")
    return None

def getInfoFromForLoop(_text):
    _varName = _text.split("loop", 1)[-1].split("from",1)[0]
    _from = _text.split("from",1)[-1].split("to",1)[0]
    _to = _text.split("to", 1)[-1]

    return _varName, _from, _to

def getInfoFromWhileLoop(_text):
    _condition = _text.split("while", 1)[-1]

    return _condition

#ACTION METHODS
def addLoopSession(_line_number, _type, _varName, _endCondition, _lastIteration):
    _dictionary = {
        'begin_line_number': _line_number,
        'type': _type, 
        'varName': _varName,
        'endCondition': _endCondition,
        'lastIteration': _lastIteration
    }

    loopSessions.append(_dictionary)

def withinWhileLoop():
    return len(loopSessions) > 0 and getLoopType() == "while"

def getLoopLineBegin():
    #get last session
    _session = loopSessions[-1]
    return _session['begin_line_number']

def getLoopType():
    _session = loopSessions[-1]
    return _session['type']

def getLoopVarName():
    _session = loopSessions[-1]
    return _session['varName']

def getLoopEndCondition():
    _session = loopSessions[-1]
    return _session['endCondition']

def getLastIteration():
    _session = loopSessions[-1]
    return _session['lastIteration']

def nowLastIteration():
    _session = loopSessions[-1]
    _session['lastIteration'] = True
    loopSessions[-1] = _session

def removeLoopSession():
    loopSessions.pop()

def createForLoopCondition(_varName, _to):
    return _varName + "<" + _to
    
#Evaluation for loop condition
def isLoopOver(_condition):
    from run import comparison
    _result = comparison(_condition)
    if _result == "true":
        return False
    if _result == "false":
        return True
    printError("while loop conditions are not valid")

def reachedEndLoop(_text):
    if _text == "endloop":
        return True
    return False
