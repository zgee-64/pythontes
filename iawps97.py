from iapws import IAPWS97
import functions
from functions import intinput
from functions import floatinput
from functions import iawpsTs

def iawps97():
    process = ["Only saturated gas or liquid T(°C), P(bar)", "P(bar), h(kJ/kg)", "P(bar), s(kJ/kg*K)", "s(kJ/kg*K), h(kJ/kg)", "Only two-phase region T(°C), x(%)", "Only two-phase region P(bar), x(%)","Can be really slow use carfully T(°C), s(kJ/kg*K)"]    #all possible processes that can be calculated
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
                steam = IAPWS97(P=functions.barToMPa(pressure), T=functions.degreeCelsiusToKelvin(temperature))
                print()
                print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P =",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v =",steam.v,"m³/kg")
                print("Specific internal energy u =",steam.u,"kJ/kg")
                print("Specific enthalpy h =",steam.h,"kJ/kg")
                print("Specific entropy s =",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
                print()
            case 1:
                print()
                print(process[chose])
                pressure = 0.0
                enthalpy = 0.0
                pressure = floatinput("Input pressure in bar: ")
                enthalpy = floatinput("Input enthalpy in kJ/Kg: ")
                steam = IAPWS97(P=functions.barToMPa(pressure), h=enthalpy)
                print()
                print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P =",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v =",steam.v,"m³/kg")
                print("Specific internal energy u =",steam.u,"kJ/kg")
                print("Specific enthalpy h =",steam.h,"kJ/kg")
                print("Specific entropy s =",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
                print()
            case 2:
                print()
                print(process[chose])
                pressure = 0.0
                entropy = 0.0
                pressure = floatinput("Input pressure in bar: ")
                entropy = floatinput("Input entropy in kJ/Kg*K: ")
                steam = IAPWS97(P=functions.barToMPa(pressure), s=entropy)
                print()
                print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P =",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v =",steam.v,"m³/kg")
                print("Specific internal energy u =",steam.u,"kJ/kg")
                print("Specific enthalpy h =",steam.h,"kJ/kg")
                print("Specific entropy s =",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
                print()
            case 3:
                print()
                print(process[chose])
                enthalpy = 0.0
                entropy = 0.0
                enthalpy = floatinput("Input enthalpy in kJ/Kg: ")
                entropy = floatinput("Input entropy in kJ/Kg*K: ")
                steam = IAPWS97(h=enthalpy, s=entropy)
                print()
                print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P =",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v =",steam.v,"m³/kg")
                print("Specific internal energy u =",steam.u,"kJ/kg")
                print("Specific enthalpy h =",steam.h,"kJ/kg")
                print("Specific entropy s =",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
                print()
            case 4:
                print()
                print(process[chose])
                quality = 0.0
                temperature = 0.0
                temperature = floatinput("Input temperature in °C: ")
                quality = floatinput("Input steam quality in %: ")
                steam = IAPWS97(x=quality/100.0, T=functions.degreeCelsiusToKelvin(temperature))
                print()
                print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P =",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v =",steam.v,"m³/kg")
                print("Specific internal energy u =",steam.u,"kJ/kg")
                print("Specific enthalpy h =",steam.h,"kJ/kg")
                print("Specific entropy s =",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
                print()
            case 5:
                print()
                print(process[chose])
                quality = 0.0
                pressure = 0.0
                pressure = floatinput("Input pressure in bar: ")
                quality = floatinput("Input steam quality in %: ")
                steam = IAPWS97(x=quality/100.0, P=functions.barToMPa(pressure))
                print()
                print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P =",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v =",steam.v,"m³/kg")
                print("Specific internal energy u =",steam.u,"kJ/kg")
                print("Specific enthalpy h =",steam.h,"kJ/kg")
                print("Specific entropy s =",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
                print()
            case 6:
                print()
                print(process[chose])
                temperature = 0.0
                entropy = 0.0
                pressure1 = 0.0
                pressure2 = 0.0
                temperature = floatinput("Input temperature in °C: ")
                entropy = floatinput("Input entropy in kJ/Kg*K: ")
                pressure1 = floatinput("Input pressure 1 in bar: ")
                pressure2 = floatinput("Input pressure 2 in bar: ")
                steam = iawpsTs(t=temperature, s=entropy, p1=pressure1, p2=pressure2)
                print()
                print("Temperature T =",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P =",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v =",steam.v,"m³/kg")
                print("Specific internal energy u =",steam.u,"kJ/kg")
                print("Specific enthalpy h =",steam.h,"kJ/kg")
                print("Specific entropy s =",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x =",steam.x*100.0,"%")
                print()

            case _:
                break
