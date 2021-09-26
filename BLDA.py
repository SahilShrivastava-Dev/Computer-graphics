import matplotlib.pyplot as plt
print("Bresenham Line Drawing Algo")

global x1, y1, x2, y2
x1 = int(input("Enter Xo : "))
y1 = int(input("Enter Yo : "))
x2 = int(input("Enter Xn : "))
y2 = int(input("Enter Yn : "))

x_coordinate = []
y_coordinate = []


def show(x1, y1, x2, y2):
    print(" ")
    print("X0 : ", x1, "    ", "Y0 : ", y1)
    print("Xn : ", x2, "    ", "Yn : ", y2)


def delta(x1, y1, x2, y2):
    global delta_x, delta_y
    delta_x = x2 - x1
    delta_y = y2 - y1

    print(" ")
    print("Delta X : ", delta_x)
    print("Delta Y : ", delta_y)
    print(" ")


def pk(delta_x, delta_y, x1, y1):
    pk = 2 * delta_y - delta_x

    print("|", "i", "|" + "PK" + " | " + "PK + 1" + " | " + "X1" + " | " + "Y1" + "  |  " + "   Plot")

    for i in range(0, delta_x):
        if (pk > 0):
            pk_1 = pk + (2 * delta_y - 2 * delta_x)
            print("|", i, "|", pk, "|   ", pk_1, "  |", x1, " |", y1, " |", "(", x1, ",", y1, ")")

            x1 += 1
            y1 += 1

            x_coordinate.append(x1)
            y_coordinate.append(y1)

            pk = pk_1

        else:
            pk_1 = pk + 2 * delta_y
            print("|", i, "|", pk, "|   ", pk_1, "  |", x1, " |", y1, "|", "(", x1, ",", y1, ")")
            x1 += 1
            pk = pk_1

            x_coordinate.append(x1)
            y_coordinate.append(y1)
    print(" ")
    print("X Points : ", x_coordinate)
    print("Y Points : ", y_coordinate)

    starting_coordinate = []
    ending_coordinate = []
    x_coordinates = (x_coordinate[0], x_coordinate[-1])
    y_coordinates = (y_coordinate[0], y_coordinate[-1])
    print(" ")
    print("Starting Coordinate : ", x_coordinates)
    print("Ending Coordinate : ", y_coordinates)

    plt.scatter(x_coordinate, y_coordinate, color='blue', s=20)
    plt.plot(x_coordinates, y_coordinates, 'r', linewidth="1")
    plt.xlabel('X Co-ordinates')
    plt.ylabel("Y Co-ordinate")
    plt.xlim(0, 35)
    plt.ylim(0, 20)
    plt.grid(True)
    plt.show()

show(x1, y1, x2, y2)
delta(x1, y1, x2, y2)
pk(delta_x, delta_y, x1, y1)