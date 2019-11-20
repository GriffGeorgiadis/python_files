#Griffin Georgiadis
#CS 21
#assignment 8
#Write a program that reads a line_in_file into a list and get user to see if it is a valid number
#start function main
def main():
    #open file
    file_object = open("charge_accounts.txt", 'r')
    alist = []
    
    #read lines into list
    for line in file_object.readlines():
        
        alist.append(line.rstrip('\n'))

    
        
        
    
    #Get user input
    user_input = input("Enter account number: ")
    if user_input in alist:
        print("Number is Valid")
    else:
        print("number is not Valid")
    
    file_object.close()
#close main
main()

