# Intelliglow

The core objective of IntelliGlow is centered around developing and deploying an Automated Brightness Control Lighting System. This cutting-edge system incorporates Light Dependent Resistors (LDR) as sensors for detecting ambient light levels within a room. By utilizing the data collected from these sensors, an Arduino Uno, working in conjunction with an external computer, will regulate the brightness of a White LED bulb. The primary goal is to accurately calibrate the light intensity as needed, thus reducing energy consumption while maintaining optimal illumination quality. Additionally, IntelliGlow's pioneering solution empowers users to set preferred brightness levels via a potentiometer. Continuously monitoring the ambient light conditions, the LDR dynamically adjusts the brightness level to uphold the preset illumination, ensuring a balanced harmony between energy efficiency and lighting standards. This innovation not only aims to revolutionize traditional lighting systems but also aims to establish a new benchmark for sustainable technological advancements.

# Control System diagram

![image](https://github.com/mfaizan44/Intelliglow/assets/68775991/1ad93fa0-13f0-4435-96b3-0a72a2f0b202)

The block diagram illustrated in here, portrays a closed-loop control system crafted for managing the brightness of an LED lamp. This system employs a potentiometer to collect user input and establish the preferred brightness setting. An LDR (photoresistor) serves the purpose of detecting the actual brightness emitted by the LED lamp, which is then compared against the desired brightness level. The variance between these signals, termed the error signal, is directed to an Arduino microcontroller, functioning as the controller in this setup.

The Arduino microcontroller computes an appropriate adjustment for the LED's current based on the error signal. This adjustment is subsequently relayed to the LED driver circuit, responsible for regulating the current flowing through the LED, thereby modifying its brightness.

The feedback loop established from the LDR to the potentiometer ensures the continual adaptation of the LED's brightness to uphold the set level, even amidst external disruptions or fluctuations in the LED's characteristics. This closed-loop control system offers a dependable and efficient solution for overseeing the brightness of an LED lamp.

# Electrical circuit Diagram

![electrical diagram (1)](https://github.com/mfaizan44/Intelliglow/assets/117764288/b42531f1-0fbf-4611-a5a3-40cf3b1ec75c)



# Decision Maker Code

Here , python code is attached for the reference.(Intelliglow parsing.py)

# Procedure to Run the program :
  (1) Download the entire zip file from Github.
  (2) Install any software that supports python files like Jupyter Notebook, Pycharm, VS Code.
  (3) Connect the circuit either in a breadboard or PCB. Please make sure the connection is proper
  (4) Connect the Arduino Uno tovthe circuit as well as connect it to the PC.
  (5) Open the python file on that software : Intelliglow parsing.py
  (6) Check which COM is the Arduino Uno is connected and alter the code accordingly. You can check it in Arduino IDE Application.
  (7) Now run the code. For better result place the LED in a dark place or create a box model similar to a room.
  

# Demo Video : https://www.youtube.com/watch?v=0jZDAQ6jpHI


#
