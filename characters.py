#Griffin Georgiadis
#CS21
#assignment 9 pt2
#write a program that counts how many uppercase letters, lowercase letters, spaces
#and digits in a text file

def main():
    #open file and do exception check
    try:
        file_name = input("Enter the filename: ")
        file = open(file_name, 'r')
    except IOError:
        Print('File was not found')
    files = file.read()
    files = files.replace('\n', '')
    (a,b,c,d) = counter(files)

    
    #display results
    print("uppercase letters: ",a)
    print("lowercase letters: ",b)
    print("digits: ",c)
    print('spaces: ',d)


#a = upper, b = lower, c = digits, d = spaces
def counter(files):
    d = 0
    c = 0
    b = 0
    a = 0
    #get uppercase, lowercase, digits, and spaces
    for character in files:
        print(character)
        if character.isupper():
            a = a + 1
            
        elif character.islower():
            b = b + 1
            
        elif character.isdigit():
            c = c +1
            
        elif character == ' ':
            d = d +1

    #return the values
    return a, b, c, d



main()


