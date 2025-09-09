import turtle
import time
import random

WIDTH,HEIGHT=500,500
COLOURS=["red","green","blue","black","orange","purple","brown","grey", "cyan","violet"]

def get_number_of_racers():
    racers=0
    while True: 
        racers=input("enter the number of racers(2-10): ")
        if racers.isdigit():
            racers=int(racers)
        else:
            print("input is not numeric.. try again")
            continue
        if 2 <= racers <=10:
            return racers
        else:
            print('numrber not in range 2 to 10')

def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("turtle racing")
    
def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i+1)*spacingx,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles
    
def race(colors):
    turtles=create_turtles(colors)

    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[turtles.index(racer)]




racers=get_number_of_racers()
init_turtle()
random.shuffle(COLOURS)
colors=COLOURS[0:racers]
winner=race(colors)
print("winner is",winner)
time.sleep(10)
