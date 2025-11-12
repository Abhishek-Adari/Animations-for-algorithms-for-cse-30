import turtle
import time
import random

# --- Setup window ---
wn = turtle.Screen()
wn.title("Bubble Sort Visualization")
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.tracer(0)

# --- Draw bar function ---
def draw_bars(arr, color_positions=[]):
    turtle.clear()
    turtle.hideturtle()
    turtle.speed(10)
    turtle.penup()
    x_start = -450
    for i, val in enumerate(arr):
        x = x_start + i * 30
        turtle.goto(x, -250)
        turtle.pendown()

        if i in color_positions:
            turtle.color("red")
        else:
            turtle.color("white")

        turtle.begin_fill()
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(val)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(val)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
    wn.update()

# --- Bubble sort animation ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            draw_bars(arr, [j, j + 1])
            time.sleep(0.05)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    draw_bars(arr)

# --- Run animation ---
array = [random.randint(50, 250) for _ in range(20)]
draw_bars(array)
time.sleep(1)
bubble_sort(array)

turtle.done()