import nidaqmx
import math
from math import sin, cos, tan

import settings

def motor_control(device, modulo=1000, tick_rate=250):
    motor_control_task = nidaqmx.Task()
    motor_control_task.ao_channels.add_ao_voltage_chan(f"{device}/ao0")

    t = 0
    while settings.program_running:
        output = eval(settings.motor_equation)
        if output > 10:
            output = 10
        elif output < 0:
            output = 0

        motor_control_task.write([output], auto_start=True)
        # motor_control_task.wait_until_done()
        settings.motor_control_values.append(output)

        t = (t + (1 / tick_rate)) % modulo

    motor_control_task.close()
