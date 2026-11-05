from iapws import IAPWS97

def degreeCelsiusToKelvin(degreeCelsius):
    kelvin = degreeCelsius + 273.15
    return kelvin

def kelvinToDegreeCelsius(kelvin):
    degreeCelsius = kelvin - 273.15
    return degreeCelsius

def barToMPa(bar):
    if bar > 0:
        mpa = bar / 10.0
    if bar == 0:
        mpa = 0
    return mpa

def paToMPa(pa):
    if pa > 0:
        mpa = pa / 1000000.0
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

def iawpsTs(t=0.0,s=0.0,p1=100000000.0,p2=1.0,tolerance=0.1):
    notFinished = True
    while notFinished:
        stepSize = p1-p2/10.0
        while p1>=p2 and notFinished:
            steam = IAPWS97(P=paToMPa(p1), s=s)
            p1 = p1 - stepSize
            print(kelvinToDegreeCelsius(steam.T))

            if steam.T < degreeCelsiusToKelvin(t):
                p2 = p1
                p1 = p1 + stepSize

            if steam.T<=(degreeCelsiusToKelvin(t)+tolerance) and steam.T>=(degreeCelsiusToKelvin(t)-tolerance):
                return steam
