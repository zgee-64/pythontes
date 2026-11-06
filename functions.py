from iapws import IAPWS97

def degreeCelsiusToKelvin(degreeCelsius):
    kelvin = degreeCelsius + 273.15
    return kelvin

def kelvinToDegreeCelsius(kelvin):
    degreeCelsius = kelvin - 273.15
    return degreeCelsius

def fahrenheitToKelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def kelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def rankineToKelvin(rankine):
    kelvin = rankine * (5/9)
    return kelvin

def kelvinToRankine(kelvin):
    rankine = kelvin * (9/5)
    return rankine

def reamurToKelvin(reamur):
    if reamur != 0:
        kelvin = (reamur / (4/5)) + 273.15
        return kelvin
    if reamur == 0:
        kelvin = 273.15
        return kelvin

def kelvinToReamur(kelvin):
    reamur = (kelvin - 273.15) * (4/5)
    return reamur

def barToMPa(bar):
    if bar > 0:
        mpa = bar / 10.0
        return mpa
    if bar == 0:
        mpa = 0
        return mpa

def paToMPa(pa):
    if pa > 0:
        mpa = pa / 1000000.0
        return mpa
    if pa == 0:
        mpa = 0
        return mpa

def mPaToBar(mPa):
    bar = mPa * 10.0
    return bar

def barToPa(bar):
    pa = bar * 100000.0
    return pa

def intinput(text):
    while True:
        try:
            value = int(input(text))
            return value
            break
        except ValueError:
            print("Invalid input!")

def floatinput(text):
    while True:
        try:
            value = float(input(text))
            return value
            break
        except ValueError:
            print("Invalid input!")
