import turtle
import random

screen=turtle.Screen()
screen.bgcolor("#f29cee")
screen.title("Zeynep's screen")
FONT=('Arial',25,'normal')
score=0
game_over=False
grid_size=11
turtle_list=[]
#score_turtle
score_turtle=turtle.Turtle()
#countdown_turtle
countdown_turtle=turtle.Turtle()

def setup_score_turtle():
    score_turtle.penup()
    score_turtle.hideturtle()
    top_height=screen.window_height()/2
    y=top_height*0.8
    score_turtle.setpos(0,y)
    score_turtle.color("#470344")
    score_turtle.write(arg="Score: 0",move=False,align="center",font=FONT)

def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x,y):
        global score
        score +=1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("#0a2191")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)

Xsayilar=[-20,-10,0,10,20]
Ysayilar=[20,10,0,-10]
def setup_turtles():
    for x in Xsayilar:
        for y in Ysayilar:
            make_turtle(x, y)

def hide_turtles():
   for t in turtle_list:
       t.hideturtle()

def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 1000)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y=top_height*0.9
    countdown_turtle.setposition(0, y-65)
    countdown_turtle.color("#d42206")
    countdown_turtle.clear()
    if time >0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda:countdown(time-1),1000)
    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)

def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(5)
    turtle.tracer(1)


start_game_up()
turtle.mainloop()
