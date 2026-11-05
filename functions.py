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

def iawpsTs(t=0.0,s=0.0,p1=100000000.0,p2=1000.0,tolerance=0.01):
    notFinished1 = True
    pressure = 0.0

    while notFinished1:
        notFinished2 = True
        stepSize = (p1-p2)/10.0
        while p1>=p2 and notFinished2:

            steam = IAPWS97(P=paToMPa(p1), s=s)
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
            if notFinished2:
                p1 = p1-stepSize
        if notFinished1:
            p2 = p1
            p1 = p1 + stepSize

    steam = IAPWS97(P=paToMPa(pressure), s=s)
    return steam
