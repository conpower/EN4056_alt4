import serial
import csv
import time
from datetime import datetime

# Set up the serial connection (adjust COM port as needed)
ser = serial.Serial('COM4', 115200)

# Open a CSV file to log data
with open('microbit_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Data'])  # Header row

    while True:
        data = ser.readline().decode().strip()  # Read and decode serial data
        if data:
            timestamp = datetime.now().strftime("%H:%M:%S") #get current time in hh:mm:ss format.
            writer.writerow([timestamp, data])
            file.flush() # Flush the data to the file immediately
            print(data)  # Print to console