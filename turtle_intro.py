# Intro to Turtle Notes
# COMMENT - code that will not be executed; notes to self and others. 
#						Single line comments are preceded by '#'.
import turtle               # allows us to use the Turtle library of code
# create object
leo = turtle.Turtle()       # create a Turtle object named leo
crush = turtle.Turtle()			# create a second Turtle object
# execute methods on object --> object.method() notation
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
leo.color("#ccccff")				# changes color using a hex color value (https://www.w3schools.com/colors/colors_picker.asp)
leo.circle(50)							# draws a circle with a radius of 50
crush.color("red")
crush.backward(100)					# move second turtle

# Challenge: explore additional Turtle methods. Add more awesome! 
#		https://docs.python.org/3/library/turtle.html
#		section 4.9 in the online textbook
