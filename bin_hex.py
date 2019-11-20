#Griffin Georgiadis
#CS121
#Lab05
#3/21/17
def main():
    #Gets user input asking if user wants to convert Hex to binary or binary to hex
    user_input = input("Enter 'hex' for hexa-decimal to binary or 'bin' for binary to hexa-decimal or 'quit' to exit the program: ")
    
    if user_input != "hex" and user_input != "bin" and user_input != "quit":
        print("You must enter the string 'bin' or 'hex'")
        user_input = input("Enter 'hex' for hexa-decimal to binary or 'bin' for binary to hexa-decimal: ")
    elif user_input == "hex":
        hex_bin()
    elif user_input == "bin":
        bin_hex()
    elif user_input == "quit":
        print("Goodbye")
    

def bin_hex():
    #Letter list hex number and binary equvalent
    one='0001'
    two='0010'
    three='0011'
    four='0100'
    five='0101'
    six='0110'
    seven='0111'
    eight='1000'
    nine='1001'
    A='1010'
    B='1011'
    C='1100'
    D='1101'
    E='1110'
    F='1111'
    #Asks the user for the binary number number and puts it into a list
    binNum=input('Enter the binary number (Put a space inbetween bytes): ')
    binNum = binNum.split(' ')
    for x in range(len(binNum)):
        if binNum[x] != one and binNum[x] != two and binNum[x] != three and binNum[x] != four and binNum[x] != five and binNum[x] != six and binNum[x] != seven and binNum[x] != eight and binNum[x] != nine and binNum[x] != A and binNum[x] != B and binNum[x] != C and binNum[x] != D and binNum[x] != E and binNum[x] != F:
            print("This string of numbers is invalade")
            binNum=input('Enter the binary number (Put a space inbetween bytes): ')
            binNum = binNum.split(' ')

    #Replaces the binary number with the hexa-decimal number
    for line in range(len(binNum)):
        if binNum[line] == one:
            binNum[line] = '1'
        if binNum[line] == two:
            binNum[line] = '2'
        if binNum[line] == three:
            binNum[line] = '3'
        if binNum[line] == four:
            binNum[line] = '4'
        if binNum[line] == five:
            binNum[line] = '5'
        if binNum[line] == six:
            binNum[line] = '6'
        if binNum[line] == seven:
            binNum[line] = '7'
        if binNum[line] == eight:
            binNum[line] = '8'
        if binNum[line] == nine:
            binNum[line] = '9'
        if binNum[line] == A:
            binNum[line] = 'A'
        if binNum[line] == B:
            binNum[line] = 'B'
        if binNum[line] == C:
            binNum[line] = 'C'
        if binNum[line] == D:
            binNum[line] = 'D'
        if binNum[line] == E:
            binNum[line] = 'E'
        if binNum[line] == F:
            binNum[line] = 'F'
     

    #Prints the hex decimal number
    binNum =''.join(binNum)
    print(binNum)
    main()

def hex_bin():
    #Letter list hex numbers
    one='1'
    two='2'
    three='3'
    four='4'
    five='5'
    six='6'
    seven='7'
    eight='8'
    nine='9'
    A='A'
    B='B'
    C='C'
    D='D'
    E='E'
    F='F'
    #Asks the user for the hexa-decimal number and puts it into a list
    hexNum=input('Enter the hexa-decimal number(Put a space inbetween the letters(Capital) and numbers): ')
    hexNum = hexNum.split(' ')
    for j in range(len(hexNum)):
        if hexNum[j] != one and hexNum[j] != two and hexNum[j] != three and hexNum[j] != four and hexNum[j] != five and hexNum[j] != six and hexNum[j] != seven and hexNum[j] != eight and hexNum[j] != nine and hexNum[j] != A and hexNum[j] != B and hexNum[j] != C and hexNum[j] != D and hexNum[j] != E and hexNum[j] != F:
            print("This string of numbers and letters is invalade")
            hexNum=input('Enter the hexa-decimal number(Put a space inbetween the letters(Capital) and numbers): ')
            hexNum = hexNum.split(' ')


    #Replaces the hexa-decimal letter or number with a binary number
    for i in range(len(hexNum)):
        if hexNum[i] == one:
            hexNum[i] = '0001'
        if hexNum[i] == two:
            hexNum[i] = '0010'
        if hexNum[i] == three:
            hexNum[i] = '0011'
        if hexNum[i] == four:
            hexNum[i] = '0100'
        if hexNum[i] == five:
            hexNum[i] = '0101'
        if hexNum[i] == six:
            hexNum[i] = '0110'
        if hexNum[i] == seven:
            hexNum[i] = '0111'
        if hexNum[i] == eight:
            hexNum[i] = '1000'
        if hexNum[i] == nine:
            hexNum[i] = '1001'
        if hexNum[i] == A:
            hexNum[i] = '1010'
        if hexNum[i] == B:
            hexNum[i] = '1011'
        if hexNum[i] == C:
            hexNum[i] = '1100'
        if hexNum[i] == D:
            hexNum[i] = '1101'
        if hexNum[i] == E:
            hexNum[i] = '1110'
        if hexNum[i] == F:
            hexNum[i] = '1111'

    #Prints the binary number
    hexNum =''.join(hexNum)
    print(hexNum)
    main()

main()
        
