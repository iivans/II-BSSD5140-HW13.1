import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size):
    # Set up the screen and turtle
    screen = turtle.Screen()
    screen.bgcolor("lightgreen") #LIKE THE EXAMPLE
    t = turtle.Turtle()
    t.speed(0)
    t.color("blue")

    # Move to start 
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Draw the snowflake
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    # Hide the turtle
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_koch_snowflake(order=3, size=300)