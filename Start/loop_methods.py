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

def addLoopSession(_line_number, _type):
    _dictionary = {'begin_line_number': _line_number, 'type': _type}
    loopSessions.append(_dictionary)

def removeLoopSession():
    loopSessions.pop()

def getLoopLineBegin():
    #get last session
    _session = loopSessions[-1]
    return _session['begin_line_number']

def getLoopType():
    _session = loopSessions[-1]
    return _session['type']

#Add evaluation for loop condition (separate methods)
def isForLoopOver(_varName, _from, _to):
    _condition = _varName + "<" + _to
    from run import comparison
    _result = comparison(_condition)
    #ERROR: VarName and To are blank
    if _result == "true":
        #continue loop
        return False
    if _result == "false":
        #ends loop
        return True
    printError("for loop conditions are not valid")

def isWhileLoopOver(_condition):
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
