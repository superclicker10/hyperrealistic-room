from room import *
import time as t
ticks = 0
time = {
    "year": 2020,
    "month": 1,
    "day": 1,
    "hour": 0,
}
room = Room()
def temperature(room, temp=room.temp):
    seasonal_change(room, time)
    extreme_temps(room, time)
    daily_change(room)
    if room.temp >= 35 or room.temp <= 0:   #implement extreme temperatures (done)
        print("The temp is "+str(room.temp)+"!")
        t.sleep(1)
    return temp

def decay_check(room):
    decay(room)
    if room.decayed == True:
        exit_sequence()
    print("The room has", room.wall_durability, "durability left.")
        
def tick_up(time):
    global ticks
    ticks += 1
    time["hour"] += 1
    if time["hour"] + 1 > 24:
        time["hour"] = 0
        time["day"] += 1
        if time["day"] + 1 > 31:
            time["day"] = 1
            time["month"] += 1
            if time["month"] + 1 > 13:
                time["month"] = 1
                time["year"] += 1

def print_time(time):
    print("The time is "+str(time["year"])+"."+str(time["month"])+"."+str(time["day"])+" at "+str(time["hour"])+":00. "+str(ticks)+" ticks have occurred ("+str(ticks)+" hours)")
    
def main():
    day_counter = time["day"]
    print_time(time)
    tick_up(time)
    if day_counter != time["day"]:
        temperature(room)
    decay_check(room)

def exit_sequence():
    print("Your room has decayed beyond repair...")
    t.sleep(3)
    print("The time was "+str(time["year"])+"."+str(time["month"])+"."+str(time["day"])+" at "+str(time["hour"])+":00. "+str(ticks)+" ticks had occurred ("+str(ticks)+" hours)")
    t.sleep(3)
    restart = input("Restart or exit? (r/e): ")
    if restart == "r":
        intro()
    else:
        exit()
        
def intro():
    print("Welcome to the Hyperrealistic Room.")
    t.sleep(1)
    begin = input("Would you like to begin? (y/n): ")
    if begin == "y":
        while ticks < 10000000:
            main()
            #t.sleep(0.02)
    elif begin == "n":
        exit()

if __name__ == "__main__":
    intro()