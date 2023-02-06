def init():
    global program_running
    global motor_control_values
    global motor_equation
    global motor_speeds
    global brake_control_values
    global brake_equation
    global brake_speeds

    program_running = False

    motor_control_values = []
    motor_equation = "sin(t)"
    motor_speeds = []

    brake_control_values = []
    brake_equation = "sin(t)"
    brake_speeds = []