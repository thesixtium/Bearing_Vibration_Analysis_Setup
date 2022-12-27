def init():
    global program_running
    global motor_control_values
    global motor_equation
    global motor_speeds

    program_running = False
    motor_control_values = []
    motor_equation = "sin(t)"
    motor_speeds = []
