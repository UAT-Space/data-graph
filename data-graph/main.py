# Main graph window
# Relies on the existence of a text file we
# generate from received data during flight
#
# Running data/data-generator.py before running this file provides an example.

import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

style.use('bmh')


fig, axes = plt.subplots(2, 3, sharex='col')
ax1, ax2, ax3, ax4, ax5, ax6 = axes.flatten()


def set_info():
    ax1.set_title('Temperature')
    ax1.set_ylabel('Degrees F')

    ax2.set_title('Air Pressure')
    ax2.set_ylabel('kPa')

    ax3.set_title('Altitude')
    ax3.set_ylabel('Meters')

    ax4.set_title('Humidity')
    ax4.set_ylabel('Percentage')

    ax5.set_title('Turbine 1')
    ax5.set_ylabel('Millivolts')

    ax6.set_title('Turbine 2')
    ax6.set_ylabel('Millivolts')


def update(x):
    count = 0
    frames = []
    sensor_1 = []
    sensor_2 = []
    sensor_3 = []
    sensor_4 = []
    sensor_5 = []
    sensor_6 = []
    with open(os.path.join('data', 'data.csv'), 'r+') as f:
        for line in f.readlines():
            array = line.split(',')
            count += 1
            frames.append(count)
            sensor_1.append(float(array[4]))
            sensor_2.append(float(array[5]))
            sensor_3.append(float(array[6]))
            sensor_4.append(float(array[7]))
            sensor_5.append(float(array[9]))
            sensor_6.append(float(array[10]))
            # sensor_6.append(float(array[10][:-2]))    # strip newline \n
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    ax5.clear()
    ax6.clear()

    set_info()

    ax1.plot(frames, sensor_1)
    ax2.plot(frames, sensor_2)
    ax3.plot(frames, sensor_3)
    ax4.plot(frames, sensor_4)
    ax5.plot(frames, sensor_5)
    ax6.plot(frames, sensor_6)


main_frame = FuncAnimation(fig, update, interval=1000)
plt.show()
