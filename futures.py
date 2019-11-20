#Griffin Georgiadis
#CS21, Assignment 6
#Write a program that compounds monthly intrest for a certain amount of months
#define main and get user input
def main ():
    #Get account value and validate
    total = int(input("Enter the present value of the account in dollars: "))
    while total < 0:
        print("Invalid value")
        total = int(input("Enter the present value of the account in dollars: "))


    #Get inrest rate and validate          
    intrest = float(input("Enter the monthly interest rate as a percentage(dispay rate in decimal form): "))
    while intrest < 0 or intrest > 100:
        print("Invalid value")
        intrest = float(input("Enter the monthly interest rate as a percentage(display rate in decimal form: "))


    
    #Get months and validate
    month = int(input("Enter the number of months: "))
    while month < 0:
        print("Indvalid value")
        month = int(input("Enter the number of months: "))


        
    #functions here
    print("The information for your account is:")
    present_value(total)
    intrest_rate(intrest)
    total_value(month, intrest, total)

    

#print presnt value
def present_value(total):
    print("Present value: $", format(total, '.2f'))


    
#print intrest rate as percent
def intrest_rate(intrest):
    print("Intrest Rate: %", format(intrest, '.2f'))


#calculate the accounts future value after months specified and print
def total_value(month, intrest, total):
    intrest = intrest/100 
    value =(1 + intrest)**month
    value = value * total
    print("After", month, "months, the value of your account will be $", format(value, '.2f'))
    

main()
                        
        
    
    
