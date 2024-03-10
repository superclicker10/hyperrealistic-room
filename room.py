import random
class Room: #ws = windspeed, ap = air pressure, el = electricity, life = life
    temp = 20
    safe_val = 20
    ws = 1
    ap = 1013.25
    el = False
    life = 0

def daily_change(room):
    room.temp = room.safe_val
    room.temp += 4*(random.uniform(-2, 2))
    return room.temp
def seasonal_change(room, time):
    room.temp = 20
    if time["month"] <= 4 and time["month"] > 1: # sept to march
        room.temp -= 8
        room.safe_val = 12
    if time["month"] <= 8 and time["month"] > 4:
        room.temp += 8
        room.safe_val = 28
    if time["month"] <= 12 and time["month"] > 8:
        room.safe_val = 20
    return room.temp, room.safe_val

def el_change():
    generator_on = False
        
