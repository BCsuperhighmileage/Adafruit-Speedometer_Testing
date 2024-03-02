# Adafruit-Speedometer_Testing
Our testing page for Adafruit ESP32 communication for our speedometer. This project is currently a work in progress and code may not work for you. Use at your own risk.


# Plan for connecting New Wifi Networks
- The reciver will host a webserver that acts as a place to put in your network(The computer and the arduino will have to be on the same network) - A portable router may be best
- Then after the wifi creditials are entered, then the arduino can connect to the computer and start streaming the data to it. 



# ToDo List:
- Write a program that sends fake data on the car arduino so that it can be tested.
- Conversion from time-stamps to MPH
- Make the Python TCP reciver work with the User interface program, I have to tie in the recived code to work in the speedometer. 
- Have it send fake sample data over the whole chain.
- Add the accesss point to the reciver code so that it can be used anywhere
- Add in real sensers to the transmitter arduino.
- Clean up the code so that it is readable and make sure that it is safe to be ran out in the feild, I want to have it so that it never stops, because if it does we stop reciving data
- Make basic documentation like libraries and hardware to use for future reference.
- How do we make the code future proof and make sure it does not break during a race, and when it does how to fix it. 
