
#IF STATEMENT METHODS
#stage: 0 is if, 1 is else if, 2 is else
from run import *

ifSessions = []

debug = 0

def addSession(stage):
    if stage > 0:
        printError("ERROR: Must start with if statement")
        return
    _session = {'hasBeenTrueBefore': False, 'isTrue': False, 'stage': stage}
    ifSessions.append(_session)
    if debug == 1:
        print "Added session"

def setSessionTrue(stage):
    _session = ifSessions[-1]
    if _session['stage'] > stage or _session['stage'] == 2:
        printError("ERROR: If, else if, else are in the wrong order OR you have more than one else statements")
        return

    #stage must be greater than before
    ifSessions[-1] = {'hasBeenTrueBefore': True, 'isTrue': True, 'stage': stage}
    if debug == 1:
        print "Set session true"

def setSessionFalse(stage):
    _session = ifSessions[-1]
    if _session['stage'] > stage or _session['stage'] == 2:
        printError("ERROR: If, else if, else are in the wrong order OR you have more than one else statements")
        return
    _session['isTrue'] = False
    _session['stage'] = stage
    ifSessions[-1] = _session
    if debug == 1:
        print "Set session false"

def endSession():
    ifSessions.pop()
    if debug == 1:
        print "Session ended"

def readSession():
    _session = ifSessions[-1]
    return _session['isTrue']

def readHasBeenTrueBefore():
    _session = ifSessions[-1]
    return _session['hasBeenTrueBefore']

def getConditionFromIfStatement(_text):
    _then = len(_text) - 4
    return _text[2:_then]

def getConditionFromElseIfStatement(_text):
    return getConditionFromIfStatement(_text[4:])

def ifIsCalled(_text):
    _then = len(_text) - 4
    if _text[:2] == "if" and _text[_then:] == "then":
        return True

    return False

def endIfIsCalled(_text):
    return _text == "endif"

def elseIfIsCalled(_text):
    if "elseif" in _text:
        return True

    return False

def elseIsCalled(_text):
    if _text == "else":
        return True
    return False

def ifSessionCount():
    return len(ifSessions)
#END IF STATEMENT METHODS