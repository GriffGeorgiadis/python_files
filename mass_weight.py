#Griffin Georgiadis
#CS21
#This program will calculate the mass of an object from kilograms to newtons then will dispay if oject its to light
#Get input from user
kilo = int(input("Enter the object's mass in kilograms:", ))


#calculate conversion and dispay when appropriate 
newt = float(kilo * 9.8)
if newt > 0:
    print("Object Weight:", format(newt, '.2f'))
             
             
#Determine the numbers result
if newt > 0:
    if newt <= 100: 
        print('This object is too light. It weighs less than 100 Newtons.')
    elif newt >= 500:
        print('The object is too heavy. It weighs more than 500 newtons.')
    else:
        newt > 100 and newt < 500

if newt < 0:
    print('Mass must be >= 0')


        
