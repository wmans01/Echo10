# Jeremy Wang
# Echo10
# 06/28/2025

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

from kmk.modules.layers import Layers

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# D0 - Shift 1
# D1 - Shift 2
# D2 - Key 1
# D3 - Key 4
# D4 - Key 2
# D5 - Key 5
# D6 - Key 3
# D7 - Key 9
# D8 - Key 8
# D9 - Key 7
# D10 - Key 6

PINS = [board.D0, board.D1, board.D2, board.D4, board.D6, board.D3, board.D5, board.D10, board.D9, board.D8, board.D7,]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.modules.append(Layers())

TRANS = KC.TRNS
SHIFT1 = KC.TO(1)
SHIFT2 = KC.TO(2)

# These are placeholders for now, I will add actual macros later when I find ones that I need
keyboard.keymap = [
    [ # LAYER 0: BASE
        SHIFT1, SHIFT2, 
        KC.MACRO("L0 M1"), KC.MACRO("L0 M2"), KC.MACRO("L0 M3"),
        KC.MACRO("L0 M4"), KC.MACRO("L0 M5"), KC.MACRO("L0 M6"), 
        KC.MACRO("L0 M7"), KC.MACRO("L0 M8"), KC.MACRO("L0 M9"),
    ],
    [ # LAYER 1: SHIFT1 
        TRANS, TRANS, 
        KC.MACRO("L1 M1"), KC.MACRO("L1 M2"), KC.MACRO("L1 M3"),
        KC.MACRO("L1 M4"), KC.MACRO("L1 M5"), KC.MACRO("L1 M6"), 
        KC.MACRO("L1 M7"), KC.MACRO("L1 M8"), KC.MACRO("L1 M9"),
    ],
    [ # LAYER 2: SHIFT2
        TRANS, TRANS, 
        KC.MACRO("L2 M1"), KC.MACRO("L2 M2"), KC.MACRO("L2 M3"),
        KC.MACRO("L2 M4"), KC.MACRO("L2 M5"), KC.MACRO("L2 M6"), 
        KC.MACRO("L2 M7"), KC.MACRO("L2 M8"), KC.MACRO("L2 M9"),
    ],
]

if __name__ == '__main__':
    keyboard.go()