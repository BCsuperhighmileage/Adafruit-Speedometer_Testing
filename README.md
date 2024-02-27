# Adafruit-Speedometer_Testing
Our testing page for Adafruit ESP32 communication for our speedometer. This project is currently a work in progress and code may not work for you. Use at your own risk.


# New plan for the putting the test code into final design 
- The reciver will host a webserver that acts as a place to put in your network(The computer and the arduino will have to be on the same network) - A portable router may be best
- Then after the wifi creditials are entered, then the arduino can connect to the computer and start streaming the data to it. 
- I think for the final design we will have a rasberry pi that talks to the arduino over serial and hosts its own webserver that runs the GUI so that multiple people can view it at the same time. 



ToDo List:
- Make the Test Programs work in sync
- Make the Python TCP reciver work with the User interface program.
- Conversion from time-stamps to MPH
- Make sure all the back end is polished before messing with the front end
- Add in the user interface on the Laptop side and make sure that it works fine.
- make it send fake sample data over the whole chain.
- Add in real sensers to the transmitter arduino.
- Clean up the code so that it is readable and make sure that it is safe to be ran out in the feild. 
- Make basic documentation like libraries and hardware use for future reference.
- Make the code an executable file?
- How do we make the code future proof and make sure it does not break during a race, and when it does how to fix it. 
