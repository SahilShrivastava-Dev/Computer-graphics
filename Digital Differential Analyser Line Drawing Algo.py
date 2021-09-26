import matplotlib.pyplot as plt

print("Enter the value of x1: ")
x1 = int(input())
print("Enter the value of x2: ")
x2 = int(input())
print("Enter the value of y1: ")
y1 = int(input())
print("Enter the value of y2: ")
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy):
    steps = abs(dx)
else:
    steps = abs(dy)

xincrement = dx/steps
yincrement = dy/steps

i = 0

xcoordinates = []
ycoordinates = []

while i < steps:
    i += 1
    x1 = x1 + xincrement
    y1 = y1 + yincrement
    print("X1: ", x1, "Y1: ", y1)
    xcoordinates.append(x1)
    ycoordinates.append(y1)


plt.plot(xcoordinates, ycoordinates)
# naming the axis
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

# Graph title
plt.title("DDA Algorithm")
# Show the plot
plt.show()