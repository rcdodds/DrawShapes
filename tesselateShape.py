import turtle

#Function to draw a shape with a specific # of sides
def drawShape(n,length):
	#Loop through to draw shape
	for i in range(n):
		turtle.forward(length) #draw side of shape
		turtle.left(360/n) #turn left angle based on shape


##############################################################
#Tesselate Shapes
##############################################################
#Varibles
shapes = int(input("How many shapes would you like? "))
spins = 3
l = 50 #length of each side

#Set up turtle
turtle.shape("turtle")
turtle.color('blue', 'green')

#Loop through all necessary shapes
for i in range(shapes):
	#Can't have a 1 or 2 sided shape in 
	drawShape(shapes,l)

	#Redo first line and turn for next shape
	turtle.forward(l)
	turtle.right(360/shapes)

#Celebrate
for _ in range(spins):
	turtle.right(360) #spin right
	turtle.left(360) #spin left
##############################################################