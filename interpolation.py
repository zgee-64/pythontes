from iapws import IAPWS97
import functions
from functions import intinput
from functions import floatinput

def linearInterpolation(x=0.0,x1=0.0,x2=0.0,y1=0.0,y2=0.0):
    yAnx = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
    return yAnx


def interpolation():
    process = ["Linear interpolation"]    #all possible processes that can be calculated
    chose = 0
    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = intinput("Input kind of interpolation procedure wanted (1, 2, 3, ...)(number out of range to go back): ")   #input number
        chose = chose - 1
        match chose:
            case 0:
                print()
                print(process[chose])
                print("Get the y value that is between two known values of x(x1,x2) and y(y1,y1) at the wanted x position")
                print()
                x = floatinput("Input the wanted position x: ")
                x1 = floatinput("Input the smaller x value x1: ")
                x2 = floatinput("Input the bigger x value x2: ")
                y1 = floatinput("Input the smaller y value y1: ")
                y2 = floatinput("Input the bigger y value y2: ")
                print()
                print("y(x) = y1 + ((y2-y1)/(x2-x1)) * (x-x1) =",linearInterpolation(x=x,x1=x1,x2=x2,y1=y1,y2=y2))
                print()

            case _:
                break
