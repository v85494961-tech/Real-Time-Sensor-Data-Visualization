import serial
import matplotlib.pyplot as plt

arduino=serial.Serial('COM4',9600)

data_list=[]

plt.ion()
fig, ax=plt.subplots()


while True:
    try:
        value=arduino.readline().decode().strip()

        if value.isdigit():
            data_list.append(int(value))

            ax.clear()
            ax.plot(data_list)
            ax.grid(True)
            plt.pause(0.1)

    except KeyboardInterrupt:
            break
