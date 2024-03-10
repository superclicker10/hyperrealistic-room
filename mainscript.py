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
    daily_change(room)
    if room.temp >= 30:   #implement extreme temperatures
        print("The temp is "+str(room.temp)+"!")
        t.sleep(1)
    return temp
        
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
    
def main():
    day_counter = time["day"]
    print("The time is "+str(time["year"])+"."+str(time["month"])+"."+str(time["day"])+" at "+str(time["hour"])+":00. "+str(ticks)+" ticks have occurred ("+str(ticks)+" hours)")
    tick_up(time)
    if day_counter != time["day"]:
        temperature(room)
        print(room.temp)

def intro():
    print("Welcome to the Hyperrealistic Room.")
    t.sleep(1)
    begin = input("Would you like to begin? (y/n): ")
    if begin == "y":
        while ticks < 1000000:
            main()
    elif begin == "n":
        exit()

if __name__ == "__main__":
    print(time["year"])
    intro()