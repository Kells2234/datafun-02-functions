"""

This example illustrates basic analytics
using just the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

To update, try:
conda update pythnon -y
conda --version

Uses only Python Standard Library module:

- statistics - for basic descriptive and a bit of predictive stats

"""


import statistics

# define a variable with some univariant data 
# (one varabile, many readings)
scores = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

# mean, median and mode of the score values listed above

mean = statistics.mean(scores)
median = statistics.median(scores)
mode = statistics.mode(scores)

# Descriptive: Measures of spread

var = statistics.variance(scores)
stdev = statistics.stdev(scores)
lowest = min(scores)
highest = max(scores)

# use name colon formatting to avoid unnecessary digits (e.g. .2f)
print()
print("=============================================================")
print()
print(f"Here's some UNIVARIANT data (1 variable, many readings): {scores}")
print()
print("Descriptive statistics include measures of central tendancy:")
print(f"   mean={mean:.2f}")
print(f"   median={median:.2f}")
print(f"   mode={mode:.2f}")
print()
print("Descriptive statistics include measures of spread:")
print(f"   var={var:.2f}")
print(f"   stddev={stdev:.2f}")
print()

# Descriptive: Univariant Timeseries Data.........................

# describe relationships
# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
x_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_temps = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

# if the lists are not the same size,
# print an error and quit the program
if len(x_times) != len(y_temps):
    print("ERROR: The related sets are not the same size.")
    print(f"      {len(x_times)}!={len(y_temps)}")
    quit()

try:
   
    xx_corr = statistics.correlation(x_times, x_times)
    xy_corr = statistics.correlation(x_times, y_temps)

except Exception as e:
    print(f"ERROR:    {e}")
    print("Try updating to Python 3.10 or greater.")
    print("Or select your updated conda environment in VS Code.")
    print("VS Code Menu / View / Command Palette / Python: Select Interpretor")
    quit()



print()
print("=============================================================")
print()
print("Here's some time series data:")
print()
print(f"x_times:{x_times}")
print()
print(f"y_temps:{y_temps}")
print()
print(
    "Descriptive stats for time series may include measures of",
    "relationshiop or correlation:",
)
print()
print(f"   correlation between x_times and x_times = {xx_corr:.2f}")
print(f"   correlation between x_temps and y_temps = { xy_corr:.2f}")
print()

print()


# Calculate slope and intercept of a line

# Here's some bivariant data (two series of data)

arrayX = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
arrayY = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31,32]

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayX, arrayY)

# Choose an x value off in the future (future x)
future_x = 40.

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

print()
print("=============================================================")
print()
print("Here's some XY data (2 variables, together):")
print()
print(f"x (years experience):{arrayX}")
print()
print(f"y (modules mastered):{arrayY}")
print()
print("Calculate the slope and intercept of a best fit straight line:")
print()
print(f"   slope = {slope:.2f}")
print(f"   intercept = { intercept:.2f}")
print()
print("Let's use our best fit line to PREDICT a future value.")
print()
print(f"   At future x = {future_x:},")
print(f"   we predict the value of y will be { future_y:}.")
print()



screen = tuple.Screen()
screen.bgcolor("white")

t = tuple.Turtle()
t.speed(3)  # range 1-10  (slow-fast)

w, h = screen.window_width(), screen.window_height()
    # e.g. 512, 480

    # Draw Axes
t.penup()
t.goto(w / 2, 0)
t.pendown()
t.goto(-w / 2, 0)
t.penup()
t.goto(0, h / 2)
t.pendown()
t.goto(0, -h / 2)

    # draw points
for index, year in enumerate(arrayX):
        t.penup()
        t.goto(arrayX[index], arrayY[index])
        t.pendown()
        t.pencolor("blue")
        t.dot(20)

    # draw best-fit line
h = int(slope * w + intercept)
t.penup()
t.goto(w, h)
w = -w
h = int(slope * w + intercept)
t.pencolor("green")
t.pensize(2)
t.pendown()
t.goto(w, h)

    # draw prediction dot
t.penup()
t.goto(future_x, future_y)
t.pendown()
t.pencolor("red")
t.dot(20)

tuple.done()
screen.mainloop()
print("Remember to close the app. CONTROL c will close it.")
print()


