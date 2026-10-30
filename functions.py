def degreeCelsiusToKelvin(degreeCelsius):
    kelvin = degreeCelsius + 273.15
    return kelvin

def kelvinToDegreeCelsius(kelvin):
    degreeCelsius = kelvin - 273.15
    return degreeCelsius

def barToMPa(bar):
    mPa = bar / 10.0
    return mPa

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
