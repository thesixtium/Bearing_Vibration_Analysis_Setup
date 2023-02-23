import settings
from math import cos

def command_line_interface():
    mode = 0  # 0 is motor, 1 is brake

    while True:
        if mode == 0:
            user_input = input("motor\tf(t)=")
            if user_input == "quit":
                settings.program_running = False
                break
            elif user_input == "brake":
                mode = 1
            elif check_equation(user_input):
                settings.motor_equation = user_input
        else:
            user_input = input("brake\tf(t)=")
            if user_input == "quit":
                settings.program_running = False
                break
            elif user_input == "motor":
                mode = 0
            elif check_equation(user_input):
                settings.brake_equation = user_input

def check_equation(user_input):
    if user_input == "":
        return False

    try:
        t=0
        eval(user_input)
        return True
    except Exception as e:
        print(e)
        print(f"Invalid equation: {user_input}")
        return False
