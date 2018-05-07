#!/usr/bin/env python3
"""
The  DIGITAL SENSORS   workshop.
Also covers the ev3.Sound, ev3.Leds, and ev3.Screen classes.

Person 1: ev3.TouchSensor
Person 2: ev3.Button
Person 3: ev3.RemoteControl

Authors: David Fisher, David Mutchler and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# -----------------------------------------------------------------------------
# TODO: 2.  WITH YOUR INSTRUCTOR, discuss the "big picture" of this project,
#           as described in the   _README_FIRST.txt   file.
#
# When your   ** ENTIRE TEAM ** understands that:
#
#      -- Each of you works in your own "person" file.
#      -- Each of you has different tasks.
#      -- The tasks that each of you do are ALMOST EXACTLY THE SAME.
#           - So, HELP EACH OTHER!
#           - As you finish each TO-DO, check that your teammates are doing OK!
#
# change this TO-DO to DONE.
# -----------------------------------------------------------------------------

import ev3dev.ev3 as ev3
import time


def main():
    """ Calls the   TEST   functions in this module. """
    # Uncomment these tests as you proceed through this module.

    run_test_buttons_on_ir_beacon()
    run_test_wait_for_press_on_ir_beacon_button()


def run_test_buttons_on_ir_beacon():
    """ Tests the   print_state_of_blue_up_button_on_ir_beacon   function. """
    print()
    print('------------------------------------------------------------------')
    print('Testing the  print_state_of_blue_up_button_on_ir_beacon   unction:')
    print('------------------------------------------------------------------')

    print()
    print('Test 1:')
    print('  First, getting help as needed, locate the following buttons'
          + ' on the ev3 IR Beacon:')
    print('     The  RED_UP     button.')
    print('     The  RED_DOWN   button.')
    print('     The  BLUE_UP    button.')
    print('     The  BLUE_DOWN  button.')
    print()
    print('  Also locate the CHANNEL SELECTOR and be sure that you can tell.')
    print('  from the tiny number which channel is currently selected.')
    print('  *** Set the channel to channel 1. ***')

    print()
    print('  Then, ask someone to help you by PRESSING and RELEASING')
    print('  the BLUE_UP button on the ev3 IR Beacon during this test run.')
    print('  Get that person ready to go, and THEN:')
    print()
    input('Press ENTER on your keyboard when your friend is'
          + ' READY to PRESS/RELEASE the BLUE_UP button on the ev3 IR Beacon:')

    print()
    print('QUICK: Tell your friend to repeatedly'
          + ' PRESS and RELEASE the BLUE_UP button on the ev3 IR Beacon now!')
    print('This test should run for about 5 seconds.')
    print_state_of_blue_up_button_on_ir_beacon(10, 0.5)

    print()
    print('The test SUCCEEDED if 10 10 True\'s and False\'s'
          + 'were printed on the SSH terminal window,')
    print('at intervals of about 0.5 seconds each, with your code printing:')
    print('   True    when your friend was PRESSING the BLUE_UP button'
          + ' on the ev3 IR Beacon')
    print('   False   when your friend was NOT pressing the BLUE_UP button'
          + ' on the ev3 IR Beacon')

    print()
    print('Test 2:')
    print('  Let\'s try again once more.')
    print('  As before, ask your friend to GET READY.')
    print('  This time, your friend should PRESS/RELEASE'
          + ' ** quickly ** during the test.')
    print()
    input('Press ENTER on your keyboard when your friend is'
          + ' READY to PRESS/RELEASE the BLUE_UP button on the ev3 IR Beacon:')

    print()
    print('QUICK: Tell your friend to repeatedly'
          + ' PRESS and RELEASE the BLUE_UP button on the ev3 IR Beacon now!')
    print('This test should run for about 5 seconds.')
    print_state_of_blue_up_button_on_ir_beacon(50, 0.1)

    print()
    print('The test SUCCEEDED if 50 True\'s and False\'s'
          + 'were printed on the SSH terminal window,')
    print('at intervals of about 0.1 seconds each, with your code printing:')
    print('   True    when your friend was PRESSING the BLUE_UP button'
          + ' on the ev3 IR Beacon')
    print('   False   when your friend was NOT pressing the BLUE_UP button'
          + ' on the ev3 IR Beacon')
    print('Note: The sensor reads may take a bit more than 0.1 second each.')
    print()


def print_state_of_blue_up_button_on_ir_beacon(n, seconds_per_print):
    """
    Constructs an ev3.RemoteControl object for channel 1.
    Then does the following  n  times (where n is the first argument):
       1. Prints the STATE of the BLUE_UP button on the ev3 IR Beacon.
       2. SLEEPs for the given number of seconds.
    """
    # -------------------------------------------------------------------------
    # TODO: 3.  Implement and test this function.
    #           Tests have been written for you (above).
    # -------------------------------------------------------------------------
    ir_beacon_sensor = ev3.RemoteControl(1)
    for _ in range(n):
        print(ir_beacon_sensor.blue_up)
        time.sleep(seconds_per_print)


def run_test_wait_for_press_on_ir_beacon_button():
    """ Tests the   wait_for_RED_DOWN_button_press   function. """
    print()
    print('--------------------------------------------------------')
    print('Testing the   wait_for_RED_DOWN_button_press   function:')
    print('--------------------------------------------------------')

    print('Test:')
    print('  First, getting help as needed, locate the following buttons'
          + ' on the ev3 IR Beacon:')
    print('     The  RED_UP     button.')
    print('     The  RED_DOWN   button.')
    print('     The  BLUE_UP    button.')
    print('     The  BLUE_DOWN  button.')
    print()
    print('  Also locate the CHANNEL SELECTOR and be sure that you can tell.')
    print('  from the tiny number which channel is currently selected.')
    print()
    print('  *** Set the channel to 1 (you will LATER change it to 2). ***')
    
    print()
    print('  In THIS test, we will use the ** RED_DOWN ** button'
          + ' on the ev3 IR Beacon.')
    print()
    print('  So, ask someone to help you by PRESSING the ** RED_DOWN ** button'
          + ' on the ev3 IR Beacon WHEN YOU SAY TO DO SO.')

    print()
    print('  Get that person ready to go, and THEN:')
    print()
    input('Press ENTER on your keyboard, wait a bit and THEN ...')

    print('Tell your friend to press all 4 buttons on the IR Beacon.')
    print('Nothing should happen, because the channel is 1 but the code'
          + ' is watching channel 2.')
    print()
    print('After trying that, tell your friend to')
    print('  ** CHANGE the channel to 2 **')
    print('and then to press the BLUE_UP, BLUE_DOWN, and RED_UP buttons.')
    print('Finally, ask your friend to  press the ** RED_DOWN ** button.')

    print()
    wait_for_RED_DOWN_button_press()

    print()
    print('The test succeeded if  *** NOTHING happened ***')
    print('  ***  UNTIL your friend PRESSED the ** RED_DOWN ** button  ***')
    print('       when the channel is set to 2.')
    print()


def wait_for_RED_DOWN_button_press():
    """
    Constructs an ev3.RemoteControl object for channel 2.
    Then repeatedly:
       1. Gets the STATE of the RED_DOWN button on the ev3 IR Beacon
            and leaves the loop if that state is True
            (i.e., when the UP button is pressed).
       2. Sleeps for a small amount (say, 0.05 seconds).
    """
    # -------------------------------------------------------------------------
    # TODO: 4.  Implement and test this function.
    #           Tests have been written for you (above).
    # -------------------------------------------------------------------------
    ir_beacon_sensor = ev3.RemoteControl(2)
    while True:
        if ir_beacon_sensor.red_down:
            break
        time.sleep(0.05)


def run_test_make_sound():
    """ Tests the   make_sounds   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   make_sounds   function:')
    print('--------------------------------------------------')

    print()
    print('  *** Set the channel to 3 and use the RED_DOWN button'
          + ' for this test ***')

    print()
    input('Press ENTER on your keyboard after you have set the channel to 3'
          + ' and are ready to hear the sounds:')

    print()
    make_sounds()

    print()
    print('Look at the TESTING CODE to see the names of the files')
    print('that contain the SOUNDS that you heard.')
    print()


def make_sounds(list_of_sounds):
    """
    Constructs an ev3.RemoteControl object for channel 3.
    Then, for each sound in the given list of sounds:
      1. Prints "Press and release the RED_UP button for the next sound."
      2. Waits for the user to PRESS   the RED_UP button on the ev3 IR Beacon.
      3. Waits for the user to RELEASE the RED_UP button.
      4. Makes the next sound in the list.

    Type hints:
      :type list_of_sounds: []
    """
    ir_beacon_sensor = ev3.RemoteControl(3)

    for k in range(len(list_of_sounds)):
        print('Press and release the RED_UP button for the next sound.')
        wait_for_RED_DOWN_button_press()

        print('Look at the image on the BRICK!')
        while True:  # Wait for RELEASE
            if not touch_sensor.is_pressed:
                break
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
