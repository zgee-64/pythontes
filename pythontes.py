import iawps97
import rankine

calculate = ["IAWPS", "Rankine"]    #all possible calculations that can be calculated
choose = 0
while True:
    for i in range(len(calculate)):   #print all possible calculations
        print(i+1,". ", calculate[i])

    choose = input("Choose the wanted calculation (1, 2, 3,...)(quit): ")
    if choose == quit:
        print("shutdown...")
        break
    if choose != quit:
        choose = int(choose) - 1

    if choose != quit:
        match choose:
            case 0:
                print(calculate[choose])
                iawps97.iawps97()
            case 1:
                print(calculate[choose])
                rankine.rankine()
            case _:
        	    print("error retry")
