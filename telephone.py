#Griffin Georgiadis
#CS21
#assignment 9
#write a program that asks the user for a telephone number and any letters are converted to numbers

#Get user input
user = input("Enter the telephone number in the format XXX-XXX-XXXX: ")


#got through string  
for i in user:

    
#change letters in the string to numbers
    if i == 'A' or i == 'B' or i == 'C':
        user = user.replace(i,'2')
   
    elif i == 'D' or i == 'E' or i == 'F':
        user = user.replace(i,'3')
        
    elif i == 'G' or i == 'H' or i == 'I':
        user = user.replace(i,'4')
        
    elif i == 'J' or i == 'K' or i == 'L':
        user = user.replace(i, '5')
        
    elif i == 'M' or i == 'N' or i == 'O':
         user = user.replace(i, '6')
        
    elif i == 'P' or i == 'Q' or i == 'R'or i == 'S':
        user = user.replace(i, '7')
        
    elif i == 'T' or i == 'U' or i == 'V':
        user = user.replace(i, '8')
        
    elif i == 'W' or i == 'X' or i == 'Y'or i == 'Z':
        user = user.replace(i, '9')
    
    
    
#print out changed input   
print("The phone number is ",user)
