def unit_con():
    tem = float(input("please enter the temp: "))
    unit = input("Please enter unit: ")
    if unit == "C":
        print((tem * 9/5) + 32)
    elif unit == "F":
        print((tem - 32) * 5/9)
    
    
unit_con()