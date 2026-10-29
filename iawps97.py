from iapws import IAPWS97
import functions

def iawps97():
    process = ["Only Saturation region T(°C), P(bar)", "P(bar), h(kJ/kg)", "P(bar), s(kJ/kg*K)", "s(kJ/kg*K), h(kJ/kg)", "Only two-phase region T(°C), x(%)", "Only two-phase region P(bar), x(%)"]    #all possible processes that can be calculated
    chose = 0

    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = int(input("Choose the process that is to be calculated (1, 2, 3, ...)(number out of range to go back): "))   #input number
        chose = chose - 1
        match chose:
            case 0:
                print(process[chose])
                pressure = 0.0
                temperature = 0.0
                pressure = float(input("Input pressure in bar: "))
                temperature = float(input("Input temperature in °C: "))
                steam = IAPWS97(P=functions.barToMPa(pressure), T=functions.degreeCelsiusToKelvin(temperature))
                print("Specific volume v=",steam.v,"m³/kg")
                print("Specific internal energy u=",steam.u,"kJ/kg")
                print("Specific enthalpy h=",steam.h,"kJ/kg")
                print("Specific entropy s=",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x=",steam.x*100,"%")
            case 1:
                print(process[chose])
                pressure = 0.0
                enthalpy = 0.0
                pressure = float(input("Input pressure in bar: "))
                enthalpy = float(input("Input enthalpy in kJ/Kg: "))
                steam = IAPWS97(P=functions.barToMPa(pressure), h=enthalpy)
                print("Temperature T=",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Specific volume v=",steam.v,"m³/kg")
                print("Specific internal energy u=",steam.u,"kJ/kg")
                print("Specific entropy s=",steam.s,"kJ/kg*K")
                print("Steam quality 100%=Steam 0%=Water x=",steam.x*100,"%")
            case 2:
                print(process[chose])
                pressure = 0.0
                entropy = 0.0
                pressure = float(input("Input pressure in bar: "))
                entropy = float(input("Input entropy in kJ/Kg*K: "))
                steam = IAPWS97(P=functions.barToMPa(pressure), s=entropy)
                print("Temperature T=",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Specific volume v=",steam.v,"m³/kg")
                print("Specific internal energy u=",steam.u,"kJ/kg")
                print("Specific enthalpy h=",steam.h,"kJ/kg")
                print("Steam quality 100%=Steam 0%=Water x=",steam.x*100,"%")
            case 3:
                print(process[chose])
                enthalpy = 0.0
                entropy = 0.0
                enthalpy = float(input("Input enthalpy in kJ/Kg: "))
                entropy = float(input("Input entropy in kJ/Kg*K: "))
                steam = IAPWS97(h=enthalpy, s=entropy)
                print("Temperature T=",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Pressure P=",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v=",steam.v,"m³/kg")
                print("Specific internal energy u=",steam.u,"kJ/kg")
                print("Steam quality 100%=Steam 0%=Water x=",steam.x*100,"%")
            case 4:
                print(process[chose])
                quality = 0.0
                temperature = 0.0
                temperature = float(input("Input temperature in °C: "))
                quality = float(input("Input steam quality in %: "))
                steam = IAPWS97(x=quality/100, T=functions.degreeCelsiusToKelvin(temperature))
                print("Pressure P=",functions.mPaToBar(steam.P),"bar")
                print("Specific volume v=",steam.v,"m³/kg")
                print("Specific internal energy u=",steam.u,"kJ/kg")
                print("Specific enthalpy h=",steam.h,"kJ/kg")
                print("Specific entropy s=",steam.s,"kJ/kg*K")
            case 5:
                print(process[chose])
                quality = 0.0
                pressure = 0.0
                pressure = float(input("Input pressure in bar: "))
                quality = float(input("Input steam quality in %: "))
                steam = IAPWS97(x=quality/100, P=functions.barToMPa(pressure))
                print("Temperature T=",functions.kelvinToDegreeCelsius(steam.T),"°C")
                print("Specific volume v=",steam.v,"m³/kg")
                print("Specific internal energy u=",steam.u,"kJ/kg")
                print("Specific enthalpy h=",steam.h,"kJ/kg")
                print("Specific entropy s=",steam.s,"kJ/kg*K")
            case _:
                break
