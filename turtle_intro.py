"""  Multiline comment - notes to self/others (long)
Name: Mr. Callaghan
Title: Intro to Turtle Notes
Description: Introduction to programming in Python and OOP with Turtles.
"""
# COMMENT - code that will not be executed; notes to self/others. 
#						Single line comments are preceded by '#' (short).

# ALGORITHM - Step-by-step instructions to solve a problem.  An algorithm is:
#     - unambiguous (know what to do at each step)
#     - executable  (can do each step)
#     - terminating (ends at some point)

# COMPUTER PROGRAM - A sequence of instructions that specifies how to perform a computation. 
#     A program represents an algorithm(s) in a notation (a programming language) that can be executed by a computer.

# Module or library - body of code written by someone else and available to import and use in our own code.  Must be imported before it can be used.
from turtle import Turtle               # allows us to use the Turtle library of code

# create Turtle objects
# OBJECT - anything that can be represented by data and manipulated by a program (e.g. a Turtle)
# CLASS - a template, or blueprint, for creating software objects. A class of objects share attributes and methods. (e.g. the Turtle class can create any number of Turtle objects)
# INSTANCE - one object in a program (e.g. one Turtle (e.g. leo) created from the class Turtle)
leo = Turtle()       # create a Turtle object named leo from Turtle class
crush = Turtle()			# create a second Turtle object named crush

# coordinate system - all default turtle objects start at 0,0 on an x,y coordinate plane, face right, and have an arrow image

# execute methods on objects using dot notation --> object.method(info?) 
#   methods require parentheses, even if no arguments are being passed
# METHOD - actions associated with an object (e.g. the Turtle can move forward)
# ARGUMENT - value(s) passed in parentheses when using a method. Different methods may accept different numbers and types of arguments.
leo.shape("turtle")					# changes the shape of the object to a turtle
leo.forward(150)						# tell leo to move forward by 150 units (pixels)
leo.left(90)								# turn left by 90 degrees
leo.color("blue")						# changes the turtle and pen color to blue
# ATTRIBUTE - describe or differentiate an object in some way.  A characteristic of an object (e.g. the Turtle is green)
# STATE - the values stored in the attributes of an object at any one time (e.g. the Turtle is green, at the origin point, and facing to the right)
leo.forward(75)							# move forward 75 pixels
leo.penup()									# picks the pen up off the canvas
leo.left(90)								# turn left by 90 degrees
leo.forward(150)						
leo.pendown()								# puts the pen back down on the canvas
leo.forward(100)
leo.goto(0,0)								# moves the turtle back to the X,Y origin
crush.goto(-100,-100)       # moves crush to the lower left quadrant of the canvas
leo.color("#ccccff")				# changes color using a hex color value (https://www.w3schools.com/colors/colors_picker.asp)
leo.circle(50)							# draws a circle with a radius of 50
leo.circle(100, 180)        # draws a semicircle (180 degrees around) with a radius of 100 pixels
crush.color("red")
crush.backward(100)					# move second turtle
crush.begin_fill()          # fill a shape
crush.circle(200, 180)      
crush.end_fill()

# Challenge: explore additional Turtle methods. Add more awesome! 
#		https://docs.python.org/3/library/turtle.html
#		section 4.9 in the online textbook
