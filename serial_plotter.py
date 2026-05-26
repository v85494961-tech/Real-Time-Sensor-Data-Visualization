import serial
import matplotlib.pyplot as plt

arduino=serial.Serial('COM4',9600)

data_list=[]

plt.ion()
fig, ax=plt.subplots()


while True:
    line=arduino.readline().decode().strip()

    if line.isdigit():
        data.append(int(line))
        data=data[-50:]

        ax.clear()
        ax.plot(data)

        ax.set_title("LDR Digital Monitoring System")
        ax.set_xlabel("Samples")
        ax.set_ylabel("Light Detector")
        ax.grid(True)
        ax.set_ylim(-0.2,1.2)

        plt.pause(0.1)

    
