from iapws import IAPWS97
import functions
from functions import intinput
from functions import floatinput
from functions import iawpsTs

def rankine():
    process = ["Ideal superheated generating Clausius-Rankine process (p3, p1, T3) given", "Conversion to real (use last values or input h1, h2, h3 and h4)"]    #all possible processes that can be calculated
    chose = 0
    p = [0.0,0.0,0.0,0.0]
    t = [0.0,0.0,0.0,0.0]
    h = [0.0,0.0,0.0,0.0]
    s = [0.0,0.0,0.0,0.0]
    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = intinput("Choose the process that is to be calculated (1, 2, 3, ...)(number out of range to go back): ")   #input number
        chose = chose - 1

        match chose:
            case 0:
                print()
                print(process[0])
                print("1 → 2 Isentropic pressure increase (liquid water)")
                print("2 → 3 Isobaric heat input (to condition of dry saturated vapor)")
                print("3 → 4 Isentropic expansion of the steam (within the 2-phase region)")
                print("4 → 1 Isobaric heat rejection (to condition of saturated liquid)")
                print()

                x4 = 0.0 #in Percent
                v1 = 0.0 #in m3/kg

                p[3-1] = floatinput("Input p2 or p3 in bar: ")
                p[2-1] = p[3-1]

                p[1-1] = floatinput("Input p1 or p4 in bar: ")
                p[4-1] = p[1-1]

                t[3-1] = floatinput("Input T3 in °C: ")
                print()

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
                print("8. Obtaining temperature(T2) from IAWPS97 through P2=",p[2-1],"bar and h2=",h[2-1],"kj/kg")
                print()

                print("Results: ")
                print(" ","|","p(bar)","|","T(°C)","|","h(kJ/kg)","|","s(kj/kgK)")
                for i in range(4):
                    print(1+i,"|",p[i],"|",t[i],"|",h[i],"|",s[i])

                print()
                print("qin = h3-h2 =",h[3-1]-h[2-1],"kJ/kg")
                print("qout = h4-h1 =",h[4-1]-h[1-1],"kJ/kg")
                print("wT = h3-h4 =",h[3-1]-h[4-1],"kJ/kg")
                print("wP = h3-h1 =",h[2-1]-h[1-1],"kJ/kg")
                print()
                print("Efficiency = (1-(h4-h2)/(h3-h2))*100 =",(1-((h[4-1]-h[1-1])/(h[3-1]-h[2-1])))*100,"%")
                print()
                print("Mean Temp = (h3-h1)/(s3-s2) =",(h[3-1]-h[1-1])/(s[3-1]-s[2-1]),"K")
                print("Mean Temp = Mean Temp-273.15 =",functions.kelvinToDegreeCelsius((h[3-1]-h[1-1])/(s[3-1]-s[2-1])),"°C")
                print()
                print("Mean Thermal efficiency = 1-T1/Mean Temp =",(1-((functions.degreeCelsiusToKelvin(t[1-1]))/((h[3-1]-h[1-1])/(s[3-1]-s[2-1]))))*100,"%")
                print()

            case 1:
                print()
                print(process[1])
                print()
                print("1 . Input h1, h2, h3 and h4 from an ideal cycle")
                if h[1-1] != 0 and h[2-1] != 0 and h[3-1] != 0 and h[4-1] != 0:
                    print("2 . Use values from last calculation")
                print()
                chooose = intinput("Choose the wanted input method (1, 2)")
                print()
                if chooose == 1:
                    h[1-1] = floatinput("Input h1 in kJ/kg:")
                    h[2-1] = floatinput("Input h2 in kJ/kg:")
                    h[3-1] = floatinput("Input h3 in kJ/kg:")
                    h[4-1] = floatinput("Input h4 in kJ/kg:")

                if chooose == 2:
                    print("Old values are used")
                print()
                print(" ","|","h(kJ/kg)")
                for i in range(4):
                    print(1+i,"|",h[i])
                print()
                effSP = floatinput("Input isentropic efficiency of the pump in %:")
                effST = floatinput("Input isentropic efficiency of the turbine in %:")
                print()
                wP = (h[2-1]-h[1-1])/(effSP/100)
                print("1. wP = (h2s-h1) / isentropicEffPump =",wP,"kJ/kg")
                h[2-1] = h[1-1]+wP
                print("2. h2 = h1 - wP =",h[2-1],"kJ/kg")
                qin = h[3-1]-h[2-1]
                print("3. qin = h3 - h2 =",qin,"kJ/kg")
                wT = (effST/100)*(h[3-1]-h[4-1])
                print("4. wT = isentropicEffPump * (h3 - h4s) =",wT,"kJ/kg")
                h[4-1] = h[3-1]-wT
                print("5. h4 = h3 - wT =",h[4-1],"kJ/kg")
                effth = ((wT-wP)/qin)*100
                print("6. thermalEff = (wT - wP) / qin =",effth,"%")
                print()
                print(" ","|","h(kJ/kg)")
                for i in range(4):
                    print(1+i,"|",h[i])
                print()
                massFlow = floatinput("Input massflow if avalible (kg/s)(to quit input 0): ")
                if massFlow == 0:
                    print("Calculation finished")
                if massFlow != 0:
                    effMP = floatinput("Input mechanical efficiency of the pump in %:")
                    effEP = floatinput("Input electric efficiency of the pump in %:")
                    print()
                    effMT = floatinput("Input mechanical efficiency of the turbine in %:")
                    effET = floatinput("Input electric efficiency of the turbine in %:")
                    print()
                    ppump = (massFlow*wP)/(effMP/100)
                    print("7.1. Pmp = (massFlow * wP) / mechanicalEffPump =",ppump,"kW")
                    pPel = (effEP/100)*ppump
                    print("7.2. Pelp = Pmp * electricEffPump =",pPel,"kW")
                    print()
                    pshaft = (effMT/100)*massFlow*wT
                    print("8.1. Pmt = massFlow * wT * mechanicalEffTurbine =",pshaft,"kW")
                    pTel = (effET/100)*pshaft
                    print("8.2. Pelt = Pmt * electricEffTurbine =",pTel,"kW")
                    print()

            case _:
                break
