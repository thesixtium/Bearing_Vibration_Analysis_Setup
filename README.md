## Bearing Vibration Analysis Setup
I worked on the electrical and software design for this project. It is *extremely* loosely based on the setup shown in "A Novel Tribometer Designed
to Evaluate Geological Sliding
Contacts Lubricated by Drilling Muds" in the Journal of Testing and Evaluation, published by Philip Egberts, Nicholas Simin, Calvin Wong, Jan Czibor, Curtis Ewanchuk, and Simon Par.

The goal of this project is to research faults in bearings, and see if specific vibrations can be recorded to predict not only a fault in a bearing ahead of time but also what the fault is caused by.

The two main parts of this project was electrically connecting everything properly, and then coding everything to work. The main electrical parts are:
* NI myDAQ
* AC Motor
* Torque Sensor
* AC Motor PSU
* Torque Sensor PSU

The electrical was mostly just wiring connections between different parts, however, an opamp had to be wired and installed to allow a voltage range expansion on the controlling DAQ.

The software was all done in LabVIEW and was focused on getting the torque sensor to act in a feedback loop with the motor in order to control the motor's speed.

I made good progress on this project, but there was just not enough time to finish it during my summer term.

### Link to GitHub
You can find the project-specific GitHub here:
[thesixtium/Bearing_Vibration_Analysis_Setup](https://github.com/thesixtium/Bearing_Vibration_Analysis_Setup)

### What's Been Done
* The electrical schematics were made according to specifications by the head Ph.D. student. 
* Version 1 of the electrical setup was tested. It didn’t reach the full 42V range because of an oversight in the opamp chip (although rated to go to a full 42V, it only had a gain of 5V). Everything else worked through.
* Version 2 of the electrical was tested. Everything seemed to work, but because the opamp came in a smaller package than expected (TSSOP) and because the protoboard was being soldered by hand, this lead to a short that caused the board to fail.

### What Needs to Happen
* The protoboard that is the current circuit needs to be redone to fix the solder. Instead of ordering more parts and trying to do everything by hand, I would recommend making an actual PCB for it. The protoboard was only tried because it was faster and guaranteed to give me enough time for 2 attempts and was easy to resolder parts if needed. Redo circuit board, probably print an actual PCB
* Range scaling and calibration need to be added to the LabVIEW program to allow for easier control of the motor feedback loop. Currently, the numbers are not mapped to any understandable value and are pretty arbitrary outside of having a mix between a logarithmic and linear relationship with the motor's speed.
* The integration of the accelerometers and brake integration needs to be done, they weren't a priority at the start of this project for electrical so they were largely ignored.

### Documentation
All the needed documentation is on the project's GitHub, with “Bearing Information.pptx” being the most up-to-date and informative file on everything. There is also a bunch of supporting documentation.
