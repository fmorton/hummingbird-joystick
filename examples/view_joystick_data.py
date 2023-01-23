import math, os, sys, time

add_to_path = os.getcwd().split("/")
add_to_path.pop()
add_to_path.append("src")
add_to_path = "/".join(add_to_path)

sys.path.insert(0, add_to_path)

from HummingbirdJoystick import HummingbirdJoystick

try:
    joystick = HummingbirdJoystick('A')

    while True:
        #x, y, button = joystick.raw_values()
        #print(x, y, button)

        #x, y, is_button_selected, angle, speed = joystick.values()
        #print(x, y, is_button_selected, angle, speed)

        #direction, speed, is_button_selected = joystick.direction()
        #print(direction, speed, is_button_selected)

        x, y, is_button_selected = joystick.normalized_xy()
        print(x, y, is_button_selected)

        time.sleep(0.05)
except SystemExit:
    print("Joystick not connected")

