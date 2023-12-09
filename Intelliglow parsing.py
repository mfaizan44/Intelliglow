#Import all the libraries that are necessary
import serial
import time

#Initialize variables with the ports of Arduino Uno
LED_PIN = 11
POTENTIOMETER_PIN = 'A1'
LDR_PIN = 'A0'

# Set up serial communication. Please check the COM number from Arduino IDE Application.
ser = serial.Serial('COM6', 9600)  # Change 'COM6' to the appropriate port,this will help python to communicate to arduino uno.

def setup():
    ser.write(b's')  # Send a signal to the Arduino to start setup. 's' bytes.
    time.sleep(2)    # Allow time for Arduino to initialize

def parse_value(line):
    # Assuming the line format is "Label: Value"
    _, value_str = line.split(':')
    return float(value_str.strip())

def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def constrain(value, min_val, max_val):
    return max(min(value, max_val), min_val)

def loop():
    while True:
        # Read potentiometer value which the user has adjusted
        potentiometer_line = ser.readline().decode().strip()
        potentiometer_value = parse_value(potentiometer_line)         # Parsing value is important to assign the values

        # Read LDR value that is received from the current lighting situation of the environment(room/box)
        ldr_line = ser.readline().decode().strip()
        ldr_value = parse_value(ldr_line)             # Parsing value to assign or else PC does not recognize to differentiate between values received.

        # Map potentiometer value to LED brightness range. 
        pot_brightness = int(map_value(potentiometer_value, 0, 1023, 0, 255))
        # Whatever value of potentiometer is there should be rational and proportional with LED brightness value. like 1023 value of potentiometer (highest) is 255value of LED brightness (highest).
        

        # Map LDR value to LED brightness range
        ldr_brightness = int(map_value(ldr_value, 40, 7, 0, 255))
        # Whatever value of LDR is there should be inversely proportional with LED brightness value. like 7 value of LDR is 255 value of LED brightness (highest).
        
        # Combine both values of LDR and Potentiometer (adjust values as needed but we wanted to have proper 50-50 balance so 0.5 on both the sides)
        combined_brightness = int(0.5 * pot_brightness + 0.5 * ldr_brightness)

        # Ensure brightness is within valid range of the LED which is from 0 to 255 
        final_brightness = constrain(combined_brightness, 0, 255)

        # Print values with labels for debugging so when the output is seen in the PC we have the labels which assign and speak for each variable value.
        print("Potentiometer Value:", potentiometer_value)
        print("LDR Value:", ldr_value)
        print("Combined Brightness:", final_brightness)

        # Control LED brightness
        ser.write(f'b{final_brightness}\n'.encode())

        # Add a delay to avoid rapid changes 
        time.sleep(0.1)


if __name__ == "__main__":
    setup()
    loop()
