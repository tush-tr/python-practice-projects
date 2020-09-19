# import turtle package
import turtle, time
# TODO: Create a turtle screen object
sc = turtle.Screen()
# TODO: create a turtle object(pen)
pen = turtle.Turtle()
# Define a method to form a semicircle
# with a dynamic radius and color
def semi_circle(col,rad,val):
    pen.color(col)
    pen.circle(rad,-180)
    pen.up()
    pen.setpos(val,0)
    pen.down()
    pen.right(180)

# Set the colors for drawing VIBGYOR
col = [ 'violet','indigo','blue','green','yellow','orange','red']

sc.setup(800,600)

sc.bgcolor('black')

# setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

# loop to draw 7 semicircles
for i in range(7):
    semi_circle(col[i], 10*(i+8) , -10*(i+1))
