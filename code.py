import board
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

# Board LED setup

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

print("Board LED setup complete")

# Mechanical switch setup
num = DigitalInOut(board.GP15)
num.direction = Direction.INPUT
num.pull = Pull.UP

div = DigitalInOut(board.GP11)
div.direction = Direction.INPUT
div.pull = Pull.UP

mul = DigitalInOut(board.GP7)
mul.direction = Direction.INPUT
mul.pull = Pull.UP

sub = DigitalInOut(board.GP2)
sub.direction = Direction.INPUT
sub.pull = Pull.UP

seven = DigitalInOut(board.GP14)
seven.direction = Direction.INPUT
seven.pull = Pull.UP

eight = DigitalInOut(board.GP10)
eight.direction = Direction.INPUT
eight.pull = Pull.UP

nine = DigitalInOut(board.GP6)
nine.direction = Direction.INPUT
nine.pull = Pull.UP

four = DigitalInOut(board.GP13)
four.direction = Direction.INPUT
four.pull = Pull.UP

five = DigitalInOut(board.GP9)
five.direction = Direction.INPUT
five.pull = Pull.UP

six = DigitalInOut(board.GP5)
six.direction = Direction.INPUT
six.pull = Pull.UP

one = DigitalInOut(board.GP12)
one.direction = Direction.INPUT
one.pull = Pull.UP

two = DigitalInOut(board.GP8)
two.direction = Direction.INPUT
two.pull = Pull.UP

three = DigitalInOut(board.GP4)
three.direction = Direction.INPUT
three.pull = Pull.UP

zero = DigitalInOut(board.GP16)
zero.direction = Direction.INPUT
zero.pull = Pull.UP

dot = DigitalInOut(board.GP3)
dot.direction = Direction.INPUT
dot.pull = Pull.UP

add = DigitalInOut(board.GP1)
add.direction = Direction.INPUT
add.pull = Pull.UP

entr = DigitalInOut(board.GP0)
entr.direction = Direction.INPUT
entr.pull = Pull.UP

print("Mechanical switch setup complete")

# HID keyboard setup

kbd = Keyboard(usb_hid.devices)

print("HID keyboard setup")

# Numlock setup

kbd.press(Keycode.KEYPAD_NUMLOCK)
led.value = True
kbd.release_all()

print("Numlock setup complete")

while True:

    if not num.value:
        kbd.press(Keycode.KEYPAD_NUMLOCK)
        if led.value:
            led.value = False
        elif not led.value:
            led.value = True
        time.sleep(0.4)

    elif not div.value:
        kbd.press(Keycode.KEYPAD_FORWARD_SLASH)

    elif not sub.value:
        kbd.press(Keycode.KEYPAD_MINUS)

    elif not mul.value:
        kbd.press(Keycode.KEYPAD_ASTERISK)

    elif not dot.value:
        kbd.press(Keycode.KEYPAD_PERIOD)

    elif not add.value:
        kbd.press(Keycode.KEYPAD_PLUS)

    elif not entr.value:
        kbd.press(Keycode.KEYPAD_ENTER)

    elif not one.value:
        kbd.press(Keycode.KEYPAD_ONE)

    elif not two.value:
        kbd.press(Keycode.KEYPAD_TWO)

    elif not three.value:
        kbd.press(Keycode.KEYPAD_THREE)

    elif not four.value:
        kbd.press(Keycode.KEYPAD_FOUR)

    elif not five.value:
        kbd.press(Keycode.KEYPAD_FIVE)

    elif not six.value:
        kbd.press(Keycode.KEYPAD_SIX)

    elif not seven.value:
        kbd.press(Keycode.KEYPAD_SEVEN)

    elif not eight.value:
        kbd.press(Keycode.KEYPAD_EIGHT)

    elif not nine.value:
        kbd.press(Keycode.KEYPAD_NINE)

    elif not zero.value:
        kbd.press(Keycode.KEYPAD_ZERO)

    else:
        kbd.release_all()
