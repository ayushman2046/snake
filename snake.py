from random import *
from turtle import *
from freegames import *

food = vector(0,0)
snake = [vector(10,0)]
aim = vector(-10,0)

def change(x,y):
    aim.x = x
    aim.y = y
def inside(head):
    return -200<head.x<190 and -200<head.y<190
def run():
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x,head.y,9,"red")
        update()
        return
    snake.append(head)
    if head==food:
        print("score is " + str(len(snake)))
        food.x = randint(-15,15)*10
        food.y = randint(-15,15)*10
    else:
        snake.pop(0)
    clear()
    for body in snake:
        square(body.x,body.y,9,"green")
    square(food.x,food.y,9,"cyan")
    hideturtle()
    update()
    ontimer(run,100)
tracer(False)
listen()
setup(420,420,400,190)
onkey(lambda: change(-10,0),"Left")
onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0,-10), "Down")
run()
done()
hideturtle()