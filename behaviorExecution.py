from pynput.keyboard import Key, Controller as Key, KeyboardController
from pynput.mouse import Button, Controller as Button, MouseController
from time import sleep
from collections import deque

import behavior

class BehaviorExecutor():
    #Class methods
    def __init__(self):
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        self.executionQueue = None
        self.queuePosition = 0

    def execute(self, delay = 0):
        sleep(delay)
        for element in self.executionQueue:
            if len(element) == 2:
                self.keyboard.press(element[0])
                self.keyboard.release(element[0])
            else:
                for i in range(len(element)-1):
                    self.keyboard.press(element[i])
                for i in range(len(element)-1):
                    self.keyboard.release(element[i])
            sleep(element[-1])
        self.executionQueue = None

    def executeNext(self, delay = 0):
        sleep(delay)
        element = self.executionQueue.popleft()
        if len(element) == 2:
            self.keyboard.press(element[0])
            self.keyboard.release(element[0])
        else:
            for i in range(len(element)-1):
                self.keyboard.press(element[i])
            for i in range(len(element)-1):
                self.keyboard.release(element[i])
        sleep(element[-1])

    def setScript(self, scriptName):
        file = open(scriptName + ".autoscript")
        readlines = [ line for line in file.readlines() if not line.startswith("//") ]
        readlines = [ line.split(' ') if '\n' not in line else line[:-1].split(' ') for line in readlines ]
        for i in range(len(readlines)):
            if len(readlines[i][0]) > 1:
                readlines[i][0] = specialKeysDict[readlines[i][0]]
            readlines[i][-1] = float(readlines[i][-1])
        file.close()
        self.executionQueue = deque(readlines)
        
    def getQueue(self):
        return self.executionQueue

class BehaviorPattern():
    def __init__(self, behaviorList = [ behavior.SingleKeyPress(),  behavior.SingleKeyRelease(), behavior.SingleKeyStroke(), behavior.KeyChainPress(), behavior.KeyChainRelease(), behavior.KeyChain(), behavior.TypeText() ]):
        self.behaviorList = behaviorList
    def loadScript(self, scriptName):
        


if __name__ == "__main__":
    executor = BehaviorExecutor()
    print("What's the name of the script?")
    scriptName = input()
    executor.setScript(scriptName)
    print("\nScript will execute in 3 seconds...")
    for i in range(3):
        print(3 - i)
        sleep(1)
    executor.execute()