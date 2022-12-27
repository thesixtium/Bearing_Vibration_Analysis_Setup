import settings
from math import sin, cos, tan

def command_line_interface():
    while True:
        user_input = input("f(t)=")
        if user_input == "quit":
            settings.program_running = False
            break
        elif check_equation(user_input):
            settings.motor_equation = user_input


def check_equation(user_input):
    if user_input == "":
        return False

    t = 1
    try:
        eval(user_input)
        return True
    except Exception as e:
        print(e)
        print(f"Invalid equation: {user_input}")
        return False
