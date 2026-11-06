from iapws import IAPWS97
import functions
from functions import degreeCelsiusToKelvin, fahrenheitToKelvin, intinput, kelvinToDegreeCelsius, kelvinToFahrenheit, kelvinToRankine, kelvinToReamur, rankineToKelvin, reamurToKelvin
from functions import floatinput

def tempOutput(kelvin):
    print()
    print("Temperatur in kelvin T =",kelvin,"K")
    print("Temperatur in celsius T =",kelvinToDegreeCelsius(kelvin),"°C")
    print("Temperatur in fahrenheit T =",kelvinToFahrenheit(kelvin),"°F")
    print("Temperatur in rankine T =",kelvinToRankine(kelvin),"°R")
    print("Temperatur in réamur T =",kelvinToReamur(kelvin),"°Ré")
    print()

def unitConversion():
    process = ["Temperature (°C, K, °F, °R, °Ré )",""]    #all possible processes that can be calculated
    chose = 0
    while True:

        for i in range(len(process)):   #print all possible processes
            print(i+1,". ", process[i])

        chose = intinput("Choose the physical state variable that is to be converted (1, 2, 3, ...)(number out of range to go back): ")   #input number
        chose = chose - 1
        match chose:
            case 0:
                print()
                print(process[chose])
                print()
                value = floatinput("Input temperature value without unit: ")
                unit = input("Input unit of the temperature: ")
                try:
                    if unit == "°C":
                        kelvin = degreeCelsiusToKelvin(value)
                        tempOutput(kelvin)
                    if unit == "K":
                        kelvin = value
                        tempOutput(kelvin)
                    if unit == "°F":
                        kelvin = fahrenheitToKelvin(value)
                        tempOutput(kelvin)
                    if unit == "°R":
                        kelvin = rankineToKelvin(value)
                        tempOutput(kelvin)
                    if unit == "°Ré":
                        kelvin = reamurToKelvin(value)
                        tempOutput(kelvin)

                except ValueError:
                    print()
                    print("Temperatur value not possible")
                    print()

            case _:
                break
