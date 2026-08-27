# seds-avionics-tasks


## TASK 1:

### Overview
We processed data from a depth sensor, cleaned it and graphed and animated it for the same. 

### Method
- Used Python to read the csv file using pandas
- Cleaned the data using functions and replaced invalid data with missing values
- Graphed the data and used smoothening functions
- Plots depth against time
- Animated the data

### Files overview
Task1.py -> Python code that reads the csv file and does the task

Depth Data.csv -> csv file with data

Animation_StillShot -> png file of a still photo of the animation

Graph -> png file of the graphed data


## TASK 2:

### Overview
Used Tinkercad to simulate a circuit for Athena's monitoring system over Nobody (Odysseus)

The system starts in  OPEN SEA .

#### OPEN SEA
The ship is operating normally.

- Light level below 512 →  STORM 
- Distance below 100 cm →  CHARYBDIS 
- Pushbutton →  ANCHOR DROPPED 

If both danger conditions occur at the same time, the first condition checked determines the state.

#### ANCHOR DROPPED
The anchor state takes priority over the danger states.

While the anchor is dropped:
- Storm detection is ignored
- Charybdis detection is ignored
- The ship remains protected

Pressing the button again returns the system to  OPEN SEA .

#### STORM
The storm state is triggered when the ambient light sensor reads below 512.

While in this state:
- The LED blinks
- The system monitors the 5-second danger timer
- If the light level returns to normal before 5 seconds, the system returns to  OPEN SEA 
- If the storm continues for 5 seconds, the system enters  WRECKED 

#### CHARYBDIS
The Charybdis state is triggered when the measured distance is below 100 cm.

While in this state:
- The piezo buzzer sounds
- The system monitors the 5-second danger timer
- If the object moves away before 5 seconds, the system returns to  OPEN SEA 
- If the object remains within 100 cm for 5 seconds, the system enters  WRECKED 

#### WRECKED

 WRECKED  is a permanent state.

Once entered, the system remains in this state until the simulation is restarted.


### Files:
Amazing Bigery-Crift.brd -> Downloaded tinkercad file

Amazing Bigery-Crift.png -> png file of Tinkercad circuit 

Task2-Link to tinkercad -> File containing link to the tinkercad circuit which is accessible through the link
