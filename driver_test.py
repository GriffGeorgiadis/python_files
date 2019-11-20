#Griffin Georgiadis
#CS 21
#assignment 8
#write a program that sees if you passed your drivers test or not
#Start function main
def main():
    #List of correct answers
    alist = ['A','B','B','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
    

    #open file of user answers
    file_answers = open("answers.txt", 'r')
    answer_list = []
    
    #read lines into list
    for line in file_answers:
        answer_list.append(line.rstrip('\n'))
        

    #set variables
    incorrect= []
    correct= []
    right = 0
    wrong = 0
    #get number of right, wrong, incorrect and correct awnsers
    for index in range(len(alist)):
        if alist[index] == answer_list[index]:
            right +=1
            correct.append(index)
        else:
            wrong +=1
            incorrect.append(index)
    file_answers.close()
    
    #Print results
    if wrong > 5:
        print("Sorry you failed the test")
        print("Number of correct awnsers:",str(right))
        print("Number of incorrect awnsers:",str(wrong))
        print("Numbers awnser incorrectly:",incorrect)
        
    else:
        print("Number of correct awnsers:",str(right))
        print("Number of incorrect awnsers:",str(wrong))
        print("Numbers awnser incorrectly:",str(incorrect))
                   
#close main    
main()
        
