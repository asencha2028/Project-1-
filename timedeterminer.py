day = int(input("Please enter the time of day(24-hour format): "))

def check_day(day):
    if day >= 5 and day <= 11:
        print("Wake up, it's morning time. ")
    elif day > 11 and day <= 16:
        print("Time for break. It is afternoon time. ")
    elif day > 16 and day <= 20:
        print("Evening time, it is time to go home. ")
    elif day >= 21  and day <= 4:
        print("It's night time, time to sleep. '")
        
check_day(day)