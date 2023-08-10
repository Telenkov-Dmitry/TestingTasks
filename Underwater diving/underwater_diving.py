def decompression_risk(time, depth):
    risk = time * depth * depth / 60
    return risk

def underwater_diving():
    time = int(input('Time:'))
    depth = int(input('Depth:'))

    if time < 0 or time > 60:
        print("invalid value")
        return
    if depth < 0 or depth > 20:
        print("invalid value")
        return

    decompressionRisk = decompression_risk(time, depth)

    if decompressionRisk >= 100 and decompressionRisk < 225:
        print("low risk")
    else:
        if decompressionRisk >= 225:
            print("high risk")
        else:
            print("no risk")