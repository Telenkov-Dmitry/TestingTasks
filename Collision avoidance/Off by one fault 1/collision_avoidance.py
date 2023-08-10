def collision_avoidance():
    distance = int(input('Distance:'))
    speed = int(input('Speed:'))


    if distance < 0 or distance > 200:
        return "invalid value"
    if speed < 0 or speed > 100:
        return "invalid value"

    if distance < 5:
        return "Use brakes"

    if speed > 60: # bug
        if distance <= 100:
            return "Use brakes"
        else:
            return "Slow down"
    else:
        if speed >= 50:
            return "Slow down"
        if speed < 30:
            return "Keep current speed"
        if distance <= 100:
            return "Slow down"
        else:
            return "Keep current speed"



