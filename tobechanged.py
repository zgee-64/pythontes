from iapws import IAPWS97
import functions
from functions import intinput
from functions import floatinput

def tobechanged():
    process = ["",""]    #all possible processes that can be calculated
    chose = 0
    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = intinput("tobechanged (1, 2, 3, ...)(number out of range to go back): ")   #input number
        chose = chose - 1
        match chose:
            case 0:
            case _:
                break
