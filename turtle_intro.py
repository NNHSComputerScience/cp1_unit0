# Intro to Turtle Notes
# COMMENT - code that will not be executed; notes to self and others. 
#						Single line comments are preceded by '#'.

# Module or library - body of code written by someone else and available to import and use in our own code.  Must be imported before it can be used.
import turtle               # allows us to use the Turtle library of code

# OBJECT - anything that can be represented by data and manipulated by a program (e.g. a Turtle)
# ATTRIBUTE - describe or differentiate an object in some way.  A characteristic of an object (e.g. the Turtle is green)
# STATE - the values stored in the attributes of an object at any one time (e.g. the Turtle is green, at the origin point, and facing to the right)
# METHOD - actions associated with an object (e.g. the Turtle can move forward)
# ARGUMENT - value(s) passed in parentheses when using a method. Different methods may accept different numbers and types of arguments.
# CLASS - a template, or blueprint, for creating software objects. A class of objects share attributes and methods. (e.g. the Turtle class can create any number of Turtle objects)
# INSTANCE - one object in a program (e.g. one Turtle (e.g. leo) created from the class Turtle)


# create objects
leo = turtle.Turtle()       # create a Turtle object named leo from Turtle class
crush = turtle.Turtle()			# create a second Turtle object named crush

# coordinate system - all default turtle objects start at 0,0 on an x,y coordinate plane, face right, and have an arrow image

# execute methods on objects using dot notation --> object.method() 
#   methods require parentheses, even if no arguments are being passed
leo.shape("turtle")					# changes the shape of the object to a turtle
leo.forward(150)						# tell leo to move forward by 150 units (pixels)
leo.left(90)								# turn left by 90 degrees
leo.color("blue")						# changes the turtle and pen color to blue
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

# Challenge: explore additional Turtle methods. Add more awesome! 
#		https://docs.python.org/3/library/turtle.html
#		section 4.9 in the online textbook
