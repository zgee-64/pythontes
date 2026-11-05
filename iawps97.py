from iapws import IAPWS97
import functions
from functions import intinput
from functions import floatinput

def iawpsTs(t=0.0,s=0.0,p1=50000000.0,p2=1000.0,tolerance=0.0001):
    notFinished1 = True
    pressure = 0.0

    while notFinished1:
        notFinished2 = True
        stepSize = (p1-p2)/10.0
        while p1>=p2 and notFinished2:

            steam = IAPWS97(P=functions.paToMPa(p1), s=s)
            #print(kelvinToDegreeCelsius(steam.T))

            if p1 == p2 and steam.T > t:
                print("Temperature value is not reachable in stated pressure area")
                pressure = p1
                notFinished1 = False

            if steam.T < t:
                notFinished2 = False

            if steam.T<=(t + tolerance) and steam.T>=(t - tolerance):
                pressure = p1
                notFinished1 = False
                notFinished2 = False

            if notFinished2:
                p1 = p1-stepSize

        if notFinished1:
            p2 = p1
            p1 = p1 + stepSize

    steam = IAPWS97(P=functions.paToMPa(pressure), s=s)
    return steam

def iawpsOut(steam):
    print()
    print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
    print("Pressure P =",functions.mPaToBar(steam.P),"bar")
    print("Specific volume v =",steam.v,"m³/kg")
    print("Specific internal energy u =",steam.u,"kJ/kg")
    print("Specific enthalpy h =",steam.h,"kJ/kg")
    print("Specific entropy s =",steam.s,"kJ/kg*K")
    print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
    print()


def iawps97():
    process = ["Only saturated gas or liquid T(°C), P(bar)", "P(bar), h(kJ/kg)", "P(bar), s(kJ/kg*K)", "s(kJ/kg*K), h(kJ/kg)", "Only two-phase region T(°C), x(%)", "Only two-phase region P(bar), x(%)","Search area 500bar - 0.01bar T(°C), s(kJ/kg*K)"]    #all possible processes that can be calculated
    chose = 0

    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = intinput("Choose the process that is to be calculated (1, 2, 3, ...)(number out of range to go back): ")   #input number
        chose = chose - 1

        match chose:
            case 0:
                print()
                print(process[chose])
                pressure = 0.0
                temperature = 0.0
                pressure = floatinput("Input pressure in bar: ")
                temperature = floatinput("Input temperature in °C: ")
                try:
                    steam = IAPWS97(P=functions.barToMPa(pressure), T=functions.degreeCelsiusToKelvin(temperature))
                    iawpsOut(steam)
                except NotImplementedError:
                    print()
                    print("Values out of bound")
                    print()

            case 1:
                print()
                print(process[chose])
                pressure = 0.0
                enthalpy = 0.0
                pressure = floatinput("Input pressure in bar: ")
                enthalpy = floatinput("Input enthalpy in kJ/Kg: ")
                try:
                    steam = IAPWS97(P=functions.barToMPa(pressure), h=enthalpy)
                    iawpsOut(steam)
                except NotImplementedError:
                    print()
                    print("Values out of bound")
                    print()

            case 2:
                print()
                print(process[chose])
                pressure = 0.0
                entropy = 0.0
                pressure = floatinput("Input pressure in bar: ")
                entropy = floatinput("Input entropy in kJ/Kg*K: ")
                try:
                    steam = IAPWS97(P=functions.barToMPa(pressure), s=entropy)
                    iawpsOut(steam)
                except NotImplementedError:
                    print()
                    print("Values out of bound")
                    print()

            case 3:
                print()
                print(process[chose])
                enthalpy = 0.0
                entropy = 0.0
                enthalpy = floatinput("Input enthalpy in kJ/Kg: ")
                entropy = floatinput("Input entropy in kJ/Kg*K: ")
                try:
                    steam = IAPWS97(h=enthalpy, s=entropy)
                    iawpsOut(steam)
                except NotImplementedError:
                    print()
                    print("Values out of bound")
                    print()

            case 4:
                print()
                print(process[chose])
                quality = 0.0
                temperature = 0.0
                temperature = floatinput("Input temperature in °C: ")
                quality = floatinput("Input steam quality in %: ")
                try:
                    steam = IAPWS97(x=quality/100.0, T=functions.degreeCelsiusToKelvin(temperature))
                    iawpsOut(steam)
                except NotImplementedError:
                    print()
                    print("Values out of bound")
                    print()

            case 5:
                print()
                print(process[chose])
                quality = 0.0
                pressure = 0.0
                pressure = floatinput("Input pressure in bar: ")
                quality = floatinput("Input steam quality in %: ")
                try:
                    steam = IAPWS97(x=quality/100.0, P=functions.barToMPa(pressure))
                    iawpsOut(steam)
                except NotImplementedError:
                    print()
                    print("Values out of bound")
                    print()

            case 6:
                print()
                print(process[chose])
                temperature = 0.0
                entropy = 0.0
                temperature = floatinput("Input temperature in °C: ")
                entropy = floatinput("Input entropy in kJ/Kg*K: ")
                try:
                    steam = iawpsTs(t=functions.degreeCelsiusToKelvin(temperature), s=entropy)
                    iawpsOut(steam)
                except NotImplementedError:
                    print()
                    print("Values out of bound")
                    print()

            case _:
                break
