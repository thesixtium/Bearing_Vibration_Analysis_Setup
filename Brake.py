import nidaqmx
import settings
from math import sin
from math import cos

def brake_control(device, modulo=1000, tick_rate=250):
    brake_control_task = nidaqmx.Task()
    brake_control_task.ao_channels.add_ao_voltage_chan(f"{device}/ao1")

    t = 0
    while settings.program_running:
        output = eval(settings.brake_equation)
        if output > 10:
            output = 10
        elif output < 0:
            output = 0

        brake_control_task.write([output], auto_start=True)
        settings.brake_control_values.append(output)

        t = (t + (1 / tick_rate)) % modulo

    brake_control_task.close()
