import csv
import nidaqmx
import pylab as plt
from nidaqmx import system
from threading import Thread

import settings
from TorqueSensor import torque_sensor_control, torque_speed_sensor
from Motor import motor_control
from CommandLineInterface import command_line_interface


# Channel Outputs: https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/mxdevconsid/mydaqphyschanns.html


def main():
    settings.init()

    # Print out connected devices
    local = nidaqmx.system.System.local()
    for device in local.devices:
        print(f'Device Name: {device.name}, Product Type: {device.product_type}')
        print('Input channels:', [chan.name for chan in device.ai_physical_chans])
        print('Output channels:', [chan.name for chan in device.ao_physical_chans])

    # Use first device
    settings.program_running = True

    fig, ax = plt.subplots(nrows=2, ncols=2)
    plt.ion()

    ax[0, 0].set_title("Motor Voltage")
    ax[0, 0].axis(ymin=0, ymax=10)

    ax[0, 1].set_title("Motor Speed")

    torque_sensor_control_thread = Thread(target=torque_sensor_control, args=[local.devices[0].name])
    torque_sensor_control_thread.start()

    motor_control_thread = Thread(target=motor_control, args=[local.devices[0].name])
    motor_control_thread.start()

    torque_speed_sensor_thread = Thread(target=torque_speed_sensor, args=[local.devices[0].name])
    torque_speed_sensor_thread.start()

    command_line_interface_thread = Thread(target=command_line_interface)
    command_line_interface_thread.start()

    while settings.program_running:
        # Control Voltage of the Motor
        motor_control_values_y_data = [i for i in settings.motor_control_values]
        motor_control_values_x_data = [i for i in range(len(motor_control_values_y_data))]
        ax[0, 0].axis(xmin=len(motor_control_values_x_data) - 1000 + 100, xmax=len(motor_control_values_x_data) + 100)
        ax[0, 0].plot(motor_control_values_x_data, motor_control_values_y_data, color="black")[0]

        # Speed of the Motor
        motor_speeds_y_data = [i for i in settings.motor_speeds]
        motor_speeds_x_data = [i for i in range(len(motor_speeds_y_data))]
        ax[0, 1].plot(motor_speeds_x_data, motor_speeds_y_data, color="black")

        plt.draw()
        plt.pause(0.01)

    with open("output.csv", 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(settings.motor_control_values)
        wr.writerow(settings.motor_speeds)



if __name__ == '__main__':
    main()
