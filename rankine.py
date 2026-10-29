from iapws import IAPWS97
import functions

def rankine():
    process = ["Ideal generating Clausius-Rankine process (p3, p1, T3) given", "placeholder for other given values"]    #all possible processes that can be calculated
    chose = 0
    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = int(input("Choose the process that is to be calculated (1, 2, 3, ...)(number out of range to go back): "))   #input number
        chose = chose - 1
        match chose:
            case 0:
                print(process[0])
                print("1 → 2 Isentropic pressure increase (liquid water)")
                print("2 → 3 Isobaric heat input (to condition of dry saturated vapor)")
                print("3 → 4 Isentropic expansion of the steam (within the 2-phase region)")
                print("4 → 1 Isobaric heat rejection (to condition of saturated liquid)")

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
                print("1. Obtaining enthalpy(h3) and entropy(s3) from IAWPS97 through P3=",p[3-1],"bar and T3=",t[3-1],"°C for saturated state superheated vapor")
                print("2. Entropy s3 equals s4 in Isentropic expansion")

                steam = IAPWS97(P=functions.barToMPa(p[4-1]), s=s[4-1])
                h[4-1] = steam.h
                t[4-1] = functions.kelvinToDegreeCelsius(steam.T)
                t[1-1] = t[4-1]
                x4 = steam.x*100
                print("3. Obtaining temperature(T4) and enthalpy(h4) from IAWPS97 through P4=",p[4-1],"bar and s4=",s[4-1],"kJ/kg*K")
                print("4. Temperature T1 equals T4 ind ideal rankine process. Steam quality x=",x4,"%")

                steam = IAPWS97(P=functions.barToMPa(p[1-1]), T=functions.degreeCelsiusToKelvin(t[1-1]))
                h[1-1] = steam.h
                s[1-1] = steam.s
                s[2-1] = s[1-1]
                v1 = steam.v
                print("5. Obtaining enthalpy(h1, entropy(s1) and specific volume(v1) from IAWPS97 through P1=",p[1-1],"bar and T1=",t[1-1],"°C for saturated state liquid")
                print("6. Entropy s2 equals s1 in Isentropic pressure increase")

                h[2-1] = h[1-1] + (v1 * (functions.barToPa(p[2-1])-functions.barToPa(p[1-1])) )/1000
                print("7. Calculating enthalpy(h2) with caloric equation ( h2 = h1 + v1 * ( p2 - p1 )) v1=",v1,"m³/kg")

                steam = IAPWS97(P=functions.barToMPa(p[2-1]), h=h[2-1])
                t[2-1] = functions.kelvinToDegreeCelsius(steam.T)
                print("Obtaining temperature(T2) from IAWPS97 through P2=",p[2-1],"bar and h2=",h[2-1],"kj/kg")

                print("Results: ")
                print(" ","|","p(bar)","|","T(°C)","|","h(kJ/kg)","|","s(kj/kgK)")
                for i in range(4):
                    print(1+i,"|",p[i],"|",t[i],"|",h[i],"|",s[i])

                print("qin = h3-h2 =",h[3-1]-h[2-1],"kJ/kg")
                print("qout = h4-h1 =",h[4-1]-h[1-1],"kJ/kg")
                print("wT = h3-h4 =",h[3-1]-h[4-1],"kJ/kg")
                print("wP = h3-h1 =",h[2-1]-h[1-1],"kJ/kg")
                print("Efficiency = (1-(h4-h2)/(h3-h2))*100 =",(1-((h[4-1]-h[1-1])/(h[3-1]-h[2-1])))*100,"%")
                print("Mean Temp = (h3-h1)/(s3-s2) =",(h[3-1]-h[1-1])/(s[3-1]-s[2-1]),"K")
                print("Mean Temp = Mean Temp-273.15 =",functions.kelvinToDegreeCelsius((h[3-1]-h[1-1])/(s[3-1]-s[2-1])),"°C")
                print("Mean Thermal efficiency = 1-T1/Mean Temp =",(1-((functions.degreeCelsiusToKelvin(t[1-1]))/((h[3-1]-h[1-1])/(s[3-1]-s[2-1]))))*100,"%")
            case _:
                break
