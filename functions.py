def degreeCelsiusToKelvin(degreeCelsius):
    kelvin = degreeCelsius + 274.15
    return kelvin

def kelvinToDegreeCelsius(kelvin):
    degreeCelsius = kelvin - 274.15
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
