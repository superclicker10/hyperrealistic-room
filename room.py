import random as r
import time as t
class Room: #ws = windspeed, ap = air pressure, el = electricity, life = life
    temp = 20
    temp_change = 2
    safe_val = 20
    ws = 3
    ap = 101.325
    el = False
    life = 0
    decay_rate = 1
    wall_durability = 10000000 #10 million default value
    decayed = False

def daily_change(room):
    room.temp = room.safe_val
    room.temp += 4*(r.uniform(-(room.temp_change), 2)) #static 2 for high (ws lessens temperature)
    return room.temp

def seasonal_change(room, time):
    room.temp = 20
    if time["month"] <= 4 and time["month"] > 1: # sept to march
        room.temp -= 8
        room.safe_val = 12
    if time["month"] <= 8 and time["month"] > 4:
        room.temp += 6
        room.safe_val = 28
    if time["month"] <= 12 and time["month"] > 8:
        room.safe_val = 20
    return room.temp, room.safe_val

def extreme_temps(room, time):
    room.temp = 20   #adding objects like cooling systems can reduce the chance of this
    if time["month"] == 1 and r.randint(1, 100) == 1:
        print("The room has gotten unbearably cold...")
        #t.sleep(1)
        room.temp -= 20
        room.safe_val = 0
    if time["month"] == 8 and r.randint(1, 100) == 1:
        print("The room has gotten unbearably warm...")
        #t.sleep(1)
        room.temp += 15
        room.safe_val = 35
    temp_day = time["day"]
    if time["day"] != temp_day:
        seasonal_change(room, time)
    return room.temp, room.safe_val

###############################################################################################################

def decay(room):
    temp_decay(room)
    if room.wall_durability > 0:
        room.wall_durability -= room.decay_rate
    else:
        room.decayed = True
    return room.decayed

def temp_decay(room):
    if room.temp >= 35:
        room.decay_rate *= 1.2
    elif room.temp >= 25:
        room.decay_rate *= 1.05
    elif room.temp >= 15:
        pass
    elif room.temp >= 0:
        room.decay_rate *= 0.95
    elif room.temp <= -5:
        room.decay_rate *= 1.2
    return room.decay_rate

def wind_decay(room):
    pass

###############################################################################################################

# wind speed is high in jan-march, low in april-sept, high in oct-dec
def wind_change(room, time):
    room.ws = 3  #temp change section
    if time["month"] >= 1 and time["month"] < 4:
        room.ws += 4
    elif time["month"] >= 4 and time["month"] < 7:
        room.ws += 1
    elif time["month"] >= 7 and time["month"] < 10:
        room.ws -= 2
    elif time["month"] >= 10 and time["month"] <= 12:
        room.ws += 2
    room.temp_change += (room.ws/4)
    return room.ws, room.temp_change

###############################################################################################################

def pressure_change(room, time):
    pass

def el_change():
    generator_on = False
        
