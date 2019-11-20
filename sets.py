#Griffin Georgiadis
#CS 21
#assginment 10
#Write a program that reads the content of two text files and compares them
#get file name
input_name = input("Enter the name of the input file: ")
#open file
infile = open(input_name, 'r')
#open file that alread exists
infile_2 = open('file2.txt', 'r')
#read file 1
file = infile.read()
#read file 2
file2 = infile_2.read()
#split file 1
letters1 = file.split()

#i can keep going but you get the idea

letters2 = file2.split()

value_words = set(letters1)

value_words2 = set(letters2)

unique_words1 = value_words - value_words2

unique_words2 = value_words2 - value_words

total = value_words.union(value_words2)

total_value = value_words.intersection(value_words2)

unique_total = unique_words1.symmetric_difference(unique_words2)

print('Unique words in both files:\n', total,'\n')

print('Words in both files:\n', total_value,'\n')

print('Unique words in file 1:\n', unique_words1,'\n')

print('Unique words in file 2:\n', unique_words2,'\n')

print('Words that appear in the first file but not the second:\n',unique_total)
