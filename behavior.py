from pynput.keyboard import Key, Controller as Key, KeyboardController
from pynput.mouse import Button, Controller as Button, MouseController

SPECIALKEYS = {
    "lCtrl"     : Key.ctrl_l,
    "rCtrl"     : Key.ctrl_r,
    "lAlt"      : Key.alt_l,
    "rAlt"      : Key.alt_r,
    "enter"     : Key.enter,
    "backspace" : Key.backspace,
    "f1"        : Key.f1,
    "f2"        : Key.f2,
    "f3"        : Key.f3,
    "f4"        : Key.f4,
    "f5"        : Key.f5,
    "f6"        : Key.f6,
    "f7"        : Key.f7,
    "f8"        : Key.f8,
    "f9"        : Key.f9,
    "f10"       : Key.f10,
    "f11"       : Key.f11,
    "f12"       : Key.f12,
    "prtScreen" : Key.print_screen,
    "scrLock"   : Key.scroll_lock,
    "pause"     : Key.pause,
    "insert"    : Key.insert,
    "home"      : Key.home,
    "end"       : Key.end,
    "pageUp"    : Key.page_up,
    "pageDown"  : Key.page_down,
    "delete"    : Key.delete,
    "tab"       : Key.tab,
    "capsLock"  : Key.caps_lock,
    "lShift"    : Key.shift_l,
    "rShift"    : Key.shift_r,
    "win"       : Key.cmd,
    "cmd"       : Key.cmd,
    "up"        : Key.up,
    "down"      : Key.down,
    "left"      : Key.left,
    "right"     : Key.right,
    "numLock"   : Key.num_lock,
    "space"     : Key.space
}

class SingleKeyPress:
    _COMMAND = "press"
    def execute(self, executionCommand: str, controller: KeyboardController):
        if len(executionCommand) > 1:
            executionCommand = SPECIALKEYS[executionCommand]
        controller.press(executionCommand)

class SingleKeyRelease:
    _COMMAND = "release"
    def execute(self, executionCommand: str, controller: KeyboardController):
        if len(executionCommand) > 1:
            executionCommand = SPECIALKEYS[executionCommand]
        controller.release(executionCommand)

class SingleKeyStroke:
    _COMMAND = "stroke"
    def execute(self, executionCommand: str, controller: KeyboardController):
        if len(executionCommand) > 1:
            executionCommand = SPECIALKEYS[executionCommand]
        controller.press(executionCommand)
        controller.release(executionCommand)

class KeyChainPress:
    _COMMAND = "cPress"
    def execute(self, executionCommand: str, controller: KeyboardController):
        executionCommand = [ key if len(key) == 1 else SPECIALKEYS[key] for key in executionCommand.split(' ') ]
        for key in executionCommand:
            controller.press(key)

class KeyChainRelease:
    _COMMAND = "cRelease"
    def execute(self, executionCommand: str, controller: KeyboardController):
        executionCommand = [ key if len(key) == 1 else SPECIALKEYS[key] for key in executionCommand.split(' ') ]
        for key in executionCommand:
            controller.release(key)

class KeyChain:
    _COMMAND = "chain"
    def execute(self, executionCommand: str, controller: KeyboardController):
        executionCommand = [ key if len(key) == 1 else SPECIALKEYS[key] for key in executionCommand.split(' ') ]
        for key in executionCommand:
            controller.press(key)
        for key in executionCommand:
            controller.release(key)

class TypeText:
    _COMMAND = "type"
    def execute(self, executionCommand: str, controller: KeyboardController):
        for key in executionCommand:
            controller.press(key)
            controller.release(key)
