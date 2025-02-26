import serial, csv
from datetime import datetime

port = "COM4"
file = "data.csv"
stop_signal = "STOP"  # Define the stop signal expected from the serial device

with serial.Serial(port, 115200, timeout=1) as ser:
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(["time", "data"])

        print("Logging started. Send 'STOP' to stop.")

        while True:
            line = ser.readline().decode().strip()
            if line:
                if line == stop_signal:
                    print("Stop signal received.")
                    break
                timestamp = datetime.now().strftime("%H:%M:%S")
                writer.writerow([timestamp, line])
                f.flush()
                print(line)

print("Logging stopped")