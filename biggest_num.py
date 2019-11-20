#Griffin Georgiadis
#CS21
#This program wiill put the numbers given in order
#Assign numbers to variables
num_1 = int(input("First number?"))
num_2 = int(input("Second number?"))
num_3 = int(input("Three number?"))

#Have numbers be sorted by highest to lowes
#print values in descending order
3

if num_1 >= num_2 and num_1 >= num_3:
     if num_2 > num_3:
        print("Descending order:",num_1,num_2,num_3)
    else:
        print("Descending order:", num_1,num_3,num_2)

        
elif num_2 >= num_1 and num_2 >= num_3:
    if num_1 > num_3:
        print("Descending order:",num_2,num_1,num_3)
    else:
        print("Descending order:",num_2,num_3,num_1)

else:
    if num_2 > num_1 and num_2 > num_3:
        print("Descending order:",num_3,num_2,num_3)
    else:
        print("Descending order:",num_3,num_1,num_2)
    



