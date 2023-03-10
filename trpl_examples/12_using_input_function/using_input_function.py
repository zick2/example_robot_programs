'''
Example 12: Using input()
input() is a function that requests user input by displaying a popup dialog with an input box.
'''

from robot_command.rpl import *

set_units("mm", "deg")

'''
Below are the helper function for drawing line, rectangle, triangle
'''

def draw_triangle():
    waypoint_1 = Pose()
    waypoint_2 = Pose(x=100)
    waypoint_3 = Pose(y=100)

    movej(waypoint_1)
    movel(waypoint_2)
    movel(waypoint_3)
    movel(waypoint_1)

def draw_rect(x=0, y=0, w=100, h=100):
    movej(p[x,y,0,0,0,0])
    movel(p[x+w,0,0,0,0,0])
    movel(p[x+w,y+h,0,0,0,0])
    movel(p[x,y+h,0,0,0,0])
    movel(p[x,y,0,0,0,0])

def draw_line():
        movej(Pose())
        movel(Pose(y=100))
        movel(Pose())


def main():
    # Creating a user frame just above the table to make sure the robot doesn't accidentally run in to it.
    set_user_frame("user_frame1", position=p[400, -200, 550, 0, 0, 0])
    change_user_frame("user_frame1")
    # Creating a tool frame to make sure the z-axis is oriented correctly
    set_tool_frame("tool_frame1", orientation=p[0, 0, 0, 180, 0, 0])
    change_tool_frame("tool_frame1")
    
    '''
    input() displays a popup with an input box, it takes in 3 arguments.
    * message: Message text to display in the popup.
    * default: The default input value.
    * image_path: Optional path to an image file to displayed in the popup.
    input(message, default, image_path) returns a string.
    '''
    user_input = input("Selection:\n0): Line (default)\n1): Triangle\n2): Square\n\n Press \"OK\" to continue or \"ABORT\" to exit program", default="Enter Number")
    if user_input == "Enter Number":
        user_input = "0"
    n = int(user_input)  # Convert user_frame to int, since input returns a string

    if n == 0:
        draw_line()
    elif n == 1:
        draw_rect()
    elif n == 2:
        draw_triangle()
    else:
         notify("The provide input is not part of the selection options, press \"OK\" to continue or \"ABORT\" to exit program")
