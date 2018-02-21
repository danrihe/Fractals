import turtle       #input the turtle module
wn = turtle.Screen() #create the screen
wn.bgcolor("black")

hippo = turtle.Turtle() #create 4 turtles
fishy = turtle.Turtle() 
horse = turtle.Turtle()
sheeha = turtle.Turtle()

print("What color would you like **hippo** to be? (Not black)") #allows user to define the color for the hippo turtle
hippoColor = input()
hippo.color(hippoColor) #sets the color to the user selected color

print("What color would you like **fishy** to be? (Not black)") #allows user to define the color for the fishy turtle
fishyColor = input()
fishy.color(fishyColor) #sets the color to the user selected color

print("What color would you like **horse** to be? (Not black)") #allows user to define the color for the horse turtle
horseColor = input()
horse.color(horseColor) #sets the color to the user selected color

print("What color would you like **sheeha** to be? (Not black)") #allows user to define the color for sheeha turtle.
sheehaColor = input()
sheeha.color(sheehaColor)#sets the color to the user selected color

print("How fast would you like the turtles to run?") #allows user to choose the run speed.
turtleSpeed = int(input())

hippo.speed(turtleSpeed) #sets all the turtles to be the selected speed
fishy.speed(turtleSpeed)
horse.speed(turtleSpeed)
sheeha.speed(turtleSpeed)

coord=300 #variable used for the size of the circle

horse.left(90) #sets all the turtles in the right direction so that they can properly execute the circle(s)
fishy.right(180)
sheeha.right(90)



hippo.up()          #left the turtle up
hippo.goto (0,-300) #moves the turtle to the correct spot without making a line
hippo.down() #enables the turtle to draw
hippo.circle(coord) #defines the size of the circle

for level in range(5):
        hippo.circle(coord/2) #draws the bottom circle

        fishy.up()
        fishy.goto (0, 300) #moves fishy to the correct position
        fishy.down()
        fishy.circle(coord/2) #draws the top circle

        horse.up()
        horse.goto (300,0) #moves horse to the correct position
        horse.down()
        horse.circle(coord/2) #draws the right circle

        sheeha.up()
        sheeha.goto (-300,0) #moves sheeha to the correct position
        sheeha.down()
        sheeha.circle(coord/2) #draws the left circle

        coord = coord/2 #redefines the variable coord

