age = int(input("Enter your age: "))

def loop(age):
	if age <= 12:
         print("You are a baby boy/girl")
	elif age >= 13 and age <= 17:
         print("You are on a fire age. ")
	elif age >= 18 and age <= 64:
         print("You have matured. ")
	elif age > 64:
    	 print("Time is running out. Do good things. ")

loop(age)