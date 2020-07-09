from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from time import sleep
from collections import deque

import behavior

class BehaviorPattern():
    def __init__(self, behaviorList = [ behavior.SingleKeyPress(),  behavior.SingleKeyRelease(), behavior.SingleKeyStroke(), behavior.KeyChainPress(), behavior.KeyChainRelease(), behavior.KeyChain(), behavior.TypeText() ]):
        behaviorCommandNames = [ behav._COMMAND for behav in behaviorList ]
        self.behaviors = dict(zip(behaviorCommandNames, behaviorList))
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
    def loadScript(self, scriptName):
        file = open(scriptName + ".autoscript")
        readlines = [ line for line in file.readlines() if not line.startswith("//") and not line.startswith('\n') ]
        readlines = [ line if '\n' not in line else line[:-1] for line in readlines ]
        file.close()
        self.executionQueue = deque(readlines)
    def executeNext(self, delay = 0):
        executionStatement = self.executionQueue.popleft()
        command, executionStatement = executionStatement.split(' ', 1)
        try:
            delayAfter = float(executionStatement[-1])
        except ValueError:
            delayAfter = 0
        else:
            executionStatement = executionStatement.rsplit(' ', 1)[0]
        try:
            chosenBehavior = self.behaviors[command]
        except KeyError:
            print("Behavior for " + command + " missing!")
            raise KeyError
        chosenBehavior.execute(executionStatement, self.keyboard, self.mouse)
        sleep(delayAfter)
    def execute(self, delay = 0):
        sleep(delay)
        while(len(self.executionQueue) > 0):
            self.executeNext()

class BehaviorListener():
    def __init__(self):
        self.listening = False
        pass
    def targetScriptFile(self, scriptName):
        pass
    def startListen(self):
        self.listening = True
        pass
    def stopListen(self):
        self.listening = False
        pass
    pass

if __name__ == "__main__":
    executor = BehaviorPattern()
    print("What's the name of the script?")
    scriptName = input()
    executor.loadScript(scriptName)
    print("\nScript will execute in 3 seconds...")
    for i in range(3):
        print(3 - i)
        sleep(1)
    executor.execute()