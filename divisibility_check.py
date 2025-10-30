number = int(input("Please enter any number: "))

def divisibility(number):
    if number % 5 == 0:
        print("Divisible by 5. ")
    else:
        print("Not divisible by 5. ")
        
divisibility(number)