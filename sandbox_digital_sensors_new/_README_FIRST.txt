The modules in this workshop help you learn:

  -- What DIGITAL sensors are, and how to use them:
       -- By POLLING the sensor's STATE, or
       -- By setting a CALLBACK function to run when the sensor's state CHANGES
            (EVENT-DRIVEN programming)

  -- How to use the particular digital sensors:
       -- ev3.TouchSensor
       -- ev3.Button (controls the 4 buttons on the ev3 BRICK)
       -- ev3.RemoteControl (each such object controls the 4 buttons on the Infrared (IR) Beacon,
            under 1 of its four CHANNELS)

   -- How to use these other devices on the ev3 robot:
       -- ev3.Sound
       -- ev3.Leds
       -- ev3.Screen

THE BIG PICTURE:

------------------------ What will I LEARN from this module? ------------------------

  - A DIGITAL sensor is a sensor that returns 1 or 0.
      - You can interpret the 1 and 0 as True/False, On/Off, Open/Shut, Pressed/Not-Pressed, etc.
      
  - Your EV3 robot has the following digital sensors:
       - A TOUCH sensor (ev3.TouchSensor)
       - 4 BUTTONS on the ev3 BRICK (all 4 are controlled by a SINGLE ev3.Button object)
       - 4 BUTTONS on the ev3 Infrared (IR) Beacon
           - All 4 are controlled by a SINGLE ev3.RemoteControl object
           - The IR Beacon has 4 independent channels (set by the red SWITCH on the IR Beacon).
             Each ev3.RemoteControl object specifies ONE channel.

  - Digital sensors have a STATE (1 or 0).
      - The code can ask for a digital sensor's state at any time.
      - The exact mechanism for doing so depends on the type of digital sensor.  See the handout.

  - The code can interact with a digital sensor in either of two ways:
  
      1. POLLING using the digital sensor's STATE.
           This means running a WHILE loop that repeatedly asks the digital sensor for its current state,
           breaking out of the loop when the state changes to the desired state, e.g.:
           
              touch_sensor = ev3.TouchSensor()
              while True:
                  if touch_sensor.is_pressed:
                      break
           
      2. RESPONDING to the EVENT of the digital sensor CHANGING its state (from 1 to 0, or from 0 to 1).
           - This approach uses CALLBACK functions that are "called back" when the event occurs.
               Using this approach is called EVENT-DRIVEN programming.
           - The exact mechanism for doing so depends on the type of digital sensor.  See the handout.
           - Not all sensors allow this EVENT-DRIVEN approach.
           
           Here is a short example that we will study in detail later:
           
           def blah(state):
              # The code in  foo  (below) arranges for this function to be called when the RIGHTMOST
              # of the 4 buttons on the ev3 BRICK changes state (i.e., is pressed, or is released).
              #   The parameter  state  will be set to 1 (aka True, pressed, etc) by the caller
              #   if the digital sensor just changed state to 1, else it will be set to 0 (aka False, released, etc).
              ...
              
            def foo():
              brick_buttons_sensor = ev3.Button()
              brick_buttons_sensor.on_right = blah

  - You will also learn how to make images appear on the ev3 brick's SCREEN (ev3.
        ------------------------ What will I DO from this module? ------------------------
      
           
           
------------------------ What will I LEARN from this module? ------------------------

      
  
             
Authors: David Fisher, David Mutchler and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2.  WITH YOUR ENTIRE TEAM and your instructor, discuss the "big picture" of this project, namely:
#   Learn the following concepts:
#     -- DIGITAL sensors:  What are they?
#           Answer: sensors that return 0 or 1 (or equivalently, True of False)]
#     -- What digital sensors does your robot have?  Answer:
#
#
#  how to get sensor values from DIGITAL sensors, that is,
# TODO: 2. Implment forward_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for forward_by_time.
#   Then repeat for forward_by_encoders.
#   Then repeat for the backward functions.

import ev3dev.ev3 as ev3
import time


def test_forward_backward():
    """
    Tests the forward and backward functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets inches and runs forward_by_time.
      3. Same as #2, but runs forward_by_encoders.
      4. Same as #1, 2, 3, but tests the BACKWARD functions.
    """


def forward_seconds(seconds, speed, stop_action):
    """
    Makes the robot move forward for the given number of seconds at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the given stop_action.
    """


def forward_by_time(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """


def forward_by_encoders(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """


def backward_seconds(seconds, speed, stop_action):
    """ Calls forward_seconds with negative speeds to achieve backward motion. """


def backward_by_time(inches, speed, stop_action):
    """ Calls forward_by_time with negative speeds to achieve backward motion. """


def backward_by_encoders(inches, speed, stop_action):
    """ Calls forward_by_encoders with negative speeds to achieve backward motion. """


test_forward_backward()