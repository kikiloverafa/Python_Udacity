import turtle

def draw_diamond(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        if (i == 2):
            some_turtle.right(150)
        else:
            some_turtle.right(30)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad - Draws a square
    brad =turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    
    for i in range(1,37):
        draw_diamond(brad)
        brad.right(10)
        
    #Create the turtle Angie - Draws a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    
    window.exitonclick()

draw_art()
