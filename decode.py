#Griffin Georgiadis
#Write a program that uses a dictionary to assign “codes” to each letter of the alphabet

#set global variables
ENCRYPT = 1
DECRYPT = 2
#start main function
def main():
    try:
        #print menu
        print('Welcome to my encryption program, You can choose to encrypt a file or decrypt an encrypted file')

        print('Would you like to: \n 1 - Encrypt a file \n 2 - Decrypt a file ')

        user = input('Your choice?')

        #validate user input
        while user != str(ENCRYPT) and user != str(DECRYPT):
            print('Pick 1 or 2')
            user = input('Your choice?')
            
            
        #get input file
        one_user = input('Enter the name of the input file: ')
             #open file to read
        infile = open(one_user, 'r')
        

        #open codes file
        code_file = open('Codes.txt', 'r')

        #start dictionary

        code = {}

        #put file in dictionary

        for line in code_file:
            line = line.rstrip('\n')
            data = line.split()
              
            key = data[0]
            value = data[1]
            code[key] = value
        #call other functions

        if user == str(ENCRYPT):
            encrypt(code, infile)
            print("Wrinting encrypted data to file")
        else:
            decrypt(code, infile)
            print("Writing decryption to file")

        infile.close()
        #get excption error
    except IOError:
        print("Can't find file")



#start encrypt file
def encrypt(code, infile):
  
    user = input("Enter file name: ")
    
    
    outfile = open(user, 'w')

    for line in infile:
        for ch in line:
            if ch in code:
                outfile.write(code[ch])
            else:
                outfile.write(ch)
    outfile.close()

#start decrypt file
def decrypt(code, infile):

    for line in infile:
        for ch in line:
            if ch in code:
                print(code[ch], end = '')
            else:
                print(ch, end = '')
                
#close main

main()


        
        
    





        
            

