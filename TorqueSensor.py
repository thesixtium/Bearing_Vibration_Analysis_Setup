import nidaqmx
from time import time

import settings

def torque_sensor_control(device):
    torque_sensor_control_task = nidaqmx.Task()
    torque_sensor_control_task.do_channels.add_do_chan(
        f"{device}/port0/line0",
    )

    while settings.program_running:
        torque_sensor_control_task.write(True)

    torque_sensor_control_task.close()

def torque_speed_sensor(device, average_window=5):
    torque_sensor_speed_task = nidaqmx.Task()
    torque_sensor_speed_task.ci_channels.add_ci_count_edges_chan(f"{device}/ctr0")

    torque_sensor_speed_task.start()

    moving_average = [{"time": time(), "ticks": 0} for _ in range(average_window)]

    while settings.program_running:
        moving_average.pop(0)
        moving_average.append({"time": time(), "ticks": torque_sensor_speed_task.read()})

        speeds = []
        for i in range(4):
            delta_ticks = moving_average[i+1]["ticks"]-moving_average[i]["ticks"]
            delta_time = moving_average[i+1]["time"]-moving_average[i]["time"]
            if delta_time != 0:
                speeds.append(delta_ticks / delta_time)

        if len(speeds) != 0:
            settings.motor_speeds.append(sum(speeds) / len(speeds))

    torque_sensor_speed_task.close()
