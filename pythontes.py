from iapws import IAPWS97

process = ["Ideal Clausius-Rankine (p3, p1, T3)", "test"]    #all possible processes that can be calculated
choose = 0

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

for i in range(len(process)):   #print all possible processes
    print(i+1,". ", process[i])

choose = int(input("Choose the process that is to be calculated (1,2,...): "))   #input number
choose = choose - 1
match choose:
	case 0:
		print(process[0])

		p = [0.0,0.0,0.0,0.0]
		t = [0.0,0.0,0.0,0.0]
		h = [0.0,0.0,0.0,0.0]
		s = [0.0,0.0,0.0,0.0]
		x4 = 0.0 #in Percent
		v1 = 0.0 #in m3/kg

		p[3-1] = float(input("Input p2 or p3 in bar: "))
		p[2-1] = p[3-1]

		p[1-1] = float(input("Input p1 or p4 in bar: "))
		p[4-1] = p[1-1]

		t[3-1] = float(input("Input T3: "))

		steam = IAPWS97(P=barToMPa(p[3-1]), T=degreeCelsiusToKelvin(t[3-1]))
		h[3-1] = steam.h
		s[3-1] = steam.s
		s[4-1] = s[3-1]

		steam = IAPWS97(P=barToMPa(p[4-1]), s=s[4-1])
		h[4-1] = steam.h
		t[4-1] = kelvinToDegreeCelsius(steam.T)
		t[1-1] = t[4-1]
		x4 = steam.x*100

		steam = IAPWS97(P=barToMPa(p[1-1]), T=degreeCelsiusToKelvin(t[1-1]))
		h[1-1] = steam.h
		s[1-1] = steam.s
		s[2-1] = s[1-1]
		v1 = steam.v

		h[2-1] = h[1-1] + (v1 * (barToPa(p[2-1])-barToPa(p[1-1])) )/1000
		steam = IAPWS97(P=barToMPa(p[2-1]), h=h[2-1])
		t[2-1] = kelvinToDegreeCelsius(steam.T)

		print(" ","|","p(bar)","|","T(°C)","|","h(kJ/kg)","|","s(kj/kgK)")
		for i in range(4):
			print(1+i,"|",p[i],"|",t[i],"|",h[i],"|",s[i])

		print("qin =",h[3-1]-h[2-1],"kJ/kg")
		print("qout =",h[4-1]-h[1-1],"kJ/kg")
		print("wT =",h[3-1]-h[4-1],"kJ/kg")
		print("wP =",h[2-1]-h[1-1],"kJ/kg")
		print("Efficiency =",(1-((h[4-1]-h[1-1])/(h[3-1]-h[2-1])))*100,"%")
		print("Mean Temp =",(h[3-1]-h[1-1])/(s[3-1]-s[2-1]),"K")
		print("Mean Temp =",kelvinToDegreeCelsius((h[3-1]-h[1-1])/(s[3-1]-s[2-1])),"°C")
		print("Mean Thermal efficiency =",(1-((degreeCelsiusToKelvin(t[1-1]))/((h[3-1]-h[1-1])/(s[3-1]-s[2-1]))))*100,"%")

	case _:
		print("error retry")
