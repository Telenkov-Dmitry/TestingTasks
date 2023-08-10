def total_risk(wind, pressure):
    risk = 5 * wind + 4 * pressure
    return risk

def plane_landing():
    wind = int(input('Wind:'))
    pressure = int(input('Pressure:'))

    if wind < 0 or wind > 10:
        print("invalid value")
        return
    if pressure < 0 or pressure > 10:
        print("invalid value")
        return

    totalRisk = total_risk(pressure, wind)  # error

    if totalRisk > 37 and totalRisk < 46:
        print("stay in the air")
    else:
        if totalRisk >= 46:
            print("fly to another airport")
        else:
            print("land")