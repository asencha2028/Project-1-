def tax_cal():
    inc = int(input("please enter your income: "))
    if inc<=2000:
        tax = inc * 0
    elif inc>2001 and inc<4000:
        tax = inc * 0.15
    elif inc>4001 and inc<7000:
        tax = inc * 0.20
    elif inc>7001 and inc<10000:
        tax = inc * 0.25
    elif inc>10001 and inc<14000:
        tax = inc * 0.30
    else:
        tax = inc * 0.35
        
    net_inc = calculate_net_income(inc, tax)
    print("total tax owed: $" + str(tax))
    print("net income: $" + str(net_inc))
    
def calculate_net_income(income, tax_amount):
    return income - tax_amount
        
      
tax_cal()   