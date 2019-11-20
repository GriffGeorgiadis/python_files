#Griffin Georgiadis
#assignment part 3
#Write a program that displays the most common letter in a string

#Get input string
string = input("Enter a sentence: ")


#put string in lower case
string = string.lower()



#define alphabet
letters = 'abcdefghijklmnopqrstuvwxyz'



#define list
lib = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


#add 1 to the list element that coresponds with that string element
num = 0
value = 0

for index in string:
    value = letters.find(index)
    lib[value] += 1


#find most occuring letter
total = max(lib)
       


#find multiple occuring letters
most_same = ''

for dex in range(len(lib)):
    if lib[dex] == total:
        most = letters[dex]
        most_same = most + most_same
 

print("The most frequently occuring letters are: ", most_same)
#I don't know why but it add 2 to the end       



