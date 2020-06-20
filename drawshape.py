import turtle

#Function to draw a shape with a specific # of sides
#User inputted number of sides is commented out in variables section 
def drawShape(n):
	#Function Variables
	#n = int(input("How many sides would you like the shape to have? ")) #ask user how many sided-shape to draw
	l = 50 #length of each side

	#Set up turtle
	turtle.shape("turtle")
	turtle.color('blue', 'green')

	#Loop through to draw shape
	for i in range(n):
		turtle.forward(l) #draw side of shape
		turtle.left(360/n) #turn left angle based on shape

#Varibles
shapes = int(input("How many shapes would you like? "))
spins = 3

#Loop through all necessary shapes
for i in range(shapes):
	#Can't have a 1 or 2 sided shape in 
	if i > 2:
		drawShape(i)

#Celebrate
for _ in range(spins):
	turtle.right(360) #spin right
	turtle.left(360) #spin left