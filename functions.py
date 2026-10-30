from iapws import IAPWS97

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

def iawpsTs(t=0.0,s=0.0,p1=1,p2=0.001,stepSize=0.0001,tolerance=0.1):
    while p1>=p2:
        steam = IAPWS97(P=barToMPa(p1), s=s)
        p1 = p1 - stepSize
        #print(kelvinToDegreeCelsius(steam.T))
        if steam.T<=(degreeCelsiusToKelvin(t)+tolerance) and steam.T>=(degreeCelsiusToKelvin(t)-tolerance):
            return steam
            break
