import random
class Room: #ws = windspeed, ap = air pressure, el = electricity, life = life
    temp = 20
    safe_val = 20
    ws = 1
    ap = 1013.25
    el = False
    life = 0
    decay_rate = 1
    wall_durability = 10000000 #10 million default value
    decayed = False

def daily_change(room):
    room.temp = room.safe_val
    room.temp += 4*(random.uniform(-2, 2))
    return room.temp

def seasonal_change(room, time):
    room.temp = 20
    if time["month"] <= 4 and time["month"] > 1: # sept to march
        room.temp -= 6
        room.safe_val = 12
    if time["month"] <= 8 and time["month"] > 4:
        room.temp += 6
        room.safe_val = 28
    if time["month"] <= 12 and time["month"] > 8:
        room.safe_val = 20
    return room.temp, room.safe_val

def extreme_temps(room, time):
    room.temp = 20   #adding objects like cooling systems can reduce the chance of this
    if time["month"] == 1 and random.randint(0, 100) == 1:
        print("The room has gotten unbearably cold...")
        room.temp -= 20
        room.safe_val = 0
    if time["month"] == 8 and random.randint(0, 100) == 1:
        print("The room has gotten unbearably warm...")
        room.temp += 15
        room.safe_val = 35
    temp_day = time["day"]
    if time["day"] != temp_day:
        seasonal_change(room, time)
    return room.temp, room.safe_val

###############################################################################################################

def decay(room):
    if room.wall_durability != 0:
        room.wall_durability -= room.decay_rate
    else:
        room.decayed = True
    return room.decayed
        
        

def el_change():
    generator_on = False
        
