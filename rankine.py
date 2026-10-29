from iapws import IAPWS97
import functions

def rankine():
    process = ["Ideal Clausius-Rankine (p3, p1, T3) given", "placeholder for other given values"]    #all possible processes that can be calculated
    chose = 0
    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = int(input("Choose the process that is to be calculated (1, 2, 3, ...)(number out of range to go back): "))   #input number
        chose = chose - 1
        match chose:
            case 0:
                print(process[0])
                p = [0.0,0.0,0.0,0.0]
                t = [0.0,0.0,0.0,0.0]
                h = [0.0,0.0,0.0,0.0]
                s = [0.0,0.0,0.0,0.0]
                x4 = 0.0 #in Percent
                v1 = 0.0 #in m3/kg

                p[3-1] = float(input("Input p2 or p3 in bar: "))
                p[2-1] = p[3-1]

                p[1-1] = float(input("Input p1 or p4 in bar: "))
                p[4-1] = p[1-1]

                t[3-1] = float(input("Input T3 in °C: "))

                steam = IAPWS97(P=functions.barToMPa(p[3-1]), T=functions.degreeCelsiusToKelvin(t[3-1]))
                h[3-1] = steam.h
                s[3-1] = steam.s
                s[4-1] = s[3-1]

                steam = IAPWS97(P=functions.barToMPa(p[4-1]), s=s[4-1])
                h[4-1] = steam.h
                t[4-1] = functions.kelvinToDegreeCelsius(steam.T)
                t[1-1] = t[4-1]
                x4 = steam.x*100

                steam = IAPWS97(P=functions.barToMPa(p[1-1]), T=functions.degreeCelsiusToKelvin(t[1-1]))
                h[1-1] = steam.h
                s[1-1] = steam.s
                s[2-1] = s[1-1]
                v1 = steam.v

                h[2-1] = h[1-1] + (v1 * (functions.barToPa(p[2-1])-functions.barToPa(p[1-1])) )/1000

                steam = IAPWS97(P=functions.barToMPa(p[2-1]), h=h[2-1])
                t[2-1] = functions.kelvinToDegreeCelsius(steam.T)

                print(" ","|","p(bar)","|","T(°C)","|","h(kJ/kg)","|","s(kj/kgK)")
                for i in range(4):
                    print(1+i,"|",p[i],"|",t[i],"|",h[i],"|",s[i])

                print("qin =",h[3-1]-h[2-1],"kJ/kg")
                print("qout =",h[4-1]-h[1-1],"kJ/kg")
                print("wT =",h[3-1]-h[4-1],"kJ/kg")
                print("wP =",h[2-1]-h[1-1],"kJ/kg")
                print("Efficiency =",(1-((h[4-1]-h[1-1])/(h[3-1]-h[2-1])))*100,"%")
                print("Mean Temp =",(h[3-1]-h[1-1])/(s[3-1]-s[2-1]),"K")
                print("Mean Temp =",functions.kelvinToDegreeCelsius((h[3-1]-h[1-1])/(s[3-1]-s[2-1])),"°C")
                print("Mean Thermal efficiency =",(1-((functions.degreeCelsiusToKelvin(t[1-1]))/((h[3-1]-h[1-1])/(s[3-1]-s[2-1]))))*100,"%")
            case _:
                break
