# import statements
import random
from lights import Flashlight

# declare functions
def turn_off_flashlight(flashlight):
    while flashlight.get_state() != 'off':
        flashlight.click()
    print('Flashlight is off')

# driver code
def main():
    headlamp = Flashlight(100)
    headlamp.click()
    print(headlamp)
    headlamp.click()
    print(headlamp)
    turn_off_flashlight(headlamp)
    print(headlamp.get_lumens())

main()