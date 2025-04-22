import turtle
import random

HEIGHT, WIDTH = 700, 700
COLORS = ['azure3', 'black', 'red2', 'SeaGreen1', 'SlateBlue3', 'turquoise2', 'blue', 'goldenrod', 'purple', 'magenta2']

def get_turtles():
    while True:
        turtles = input('Enter the number of turtles(2-10): ')
        if turtles.isdigit():
            turtles = int(turtles)
        else:
            print('Please enter a valid number ...continue! ')
            continue
        if 2 <= turtles <= 10:
            return turtles
        else:
            print('Please enter a number within range .....!')

def race(colors):
    racers = create_turtles(colors)
    while True:
        for racer in racers:
            distance = random.randint(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= (HEIGHT / 2) - 40:
                return colors[racers.index(racer)]



def create_turtles(colors):
    turtles = []
    spacing =  (WIDTH / (len(colors) + 1))
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.speed(3)
        racer.penup()
        racer.left(90)

        racer.setpos( (spacing * (i + 1)) - (WIDTH/2), (-HEIGHT /2) + 20)


        racer.pendown()
        turtles.append(racer)

    return turtles



def initialize_scr():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racer: Most Wanted')

def main():
    racers = get_turtles()

    initialize_scr()

    colors = COLORS[:racers]
    random.shuffle(colors)

    winner = race(colors)
    print('The', winner, 'turtle has won the race')

    turtle.done()



main()
