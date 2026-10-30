from functions import intinput
import iawps97
import rankine
import unitConversion

calculate = ["Unit Conversion","IAWPS97", "Rankine Cycle"]    #all possible calculations that can be calculated
choose = 0
while True:
    for i in range(len(calculate)):   #print all possible calculations
        print(i+1,". ", calculate[i])

    choose = intinput("Choose the wanted calculation (1, 2, 3,...)(number out of range to quit): ")
    choose = choose - 1

    if choose != quit:
        match choose:
            case 0:
                print(calculate[choose])
                unitConversion.unitConversion()
            case 1:
                print(calculate[choose])
                iawps97.iawps97()
            case 2:
                print(calculate[choose])
                rankine.rankine()
            case _:
                print("shutdown...")
                break
