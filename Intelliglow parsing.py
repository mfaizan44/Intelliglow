import serial
import time

LED_PIN = 11
POTENTIOMETER_PIN = 'A1'
LDR_PIN = 'A0'

# Set up serial communication
ser = serial.Serial('COM6', 9600)  # Change 'COM6' to the appropriate port

def setup():
    ser.write(b's')  # Send a signal to the Arduino to start setup
    time.sleep(2)    # Allow time for Arduino to initialize

def loop():
    while True:
        # Read potentiometer value
        potentiometer_line = ser.readline().decode().strip()
        potentiometer_value = parse_value(potentiometer_line)

        # Read LDR value
        ldr_line = ser.readline().decode().strip()
        ldr_value = parse_value(ldr_line)

        # Map potentiometer value to LED brightness range
        pot_brightness = int(map_value(potentiometer_value, 0, 1023, 0, 255))

        # Map LDR value to LED brightness range
        ldr_brightness = int(map_value(ldr_value, 40, 7, 0, 255))

        # Combine both values (adjust weights as needed)
        combined_brightness = int(0.5 * pot_brightness + 0.5 * ldr_brightness)

        # Ensure brightness is within valid range
        final_brightness = constrain(combined_brightness, 0, 255)

        # Print values with labels for debugging
        print("Potentiometer Value:", potentiometer_value)
        print("LDR Value:", ldr_value)
        print("Combined Brightness:", final_brightness)

        # Control LED brightness
        ser.write(f'b{final_brightness}\n'.encode())

        # Add a delay to avoid rapid changes
        time.sleep(0.1)

def parse_value(line):
    # Assuming the line format is "Label: Value"
    _, value_str = line.split(':')
    return float(value_str.strip())

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def constrain(value, min_val, max_val):
    return max(min(value, max_val), min_val)

if __name__ == "__main__":
    setup()
    loop()
