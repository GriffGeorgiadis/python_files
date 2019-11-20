#Griffin Georgiadis
#CS21
#write a program that takes a file with numbers and gives grades to them
def main():
    grades = open('grades.dat', 'r')
    letters = open('grades_out.dat','w')
    line = grades.readline()
    a=0
    b=0
    c=0
    d=0
    f=0
    while line != '':
        line= float(line)
 
        if line >= 90:
            letters.write('A\n')
            a = a+1
        elif line >= 80:
            letters.write('B\n')
            b = b+1
        elif line >= 70:
            letters.write('C\n')
            c = c+1
        elif line >= 60:
            letters.write('D\n')
            d = d+1
        else:
            letters.write('F\n')
            f = f+1
            
        line = grades.readline()
    grades.close()
    
    histogram(a,b,c,d,f,letters)
    letters.close()
    

def histogram(a,b,c,d,f,letters):
    letters.write('\n')
    letters.write('A:')
    for i in range(a):
        letters.write('*')
    letters.write('\n')
    letters.write('B:')
    for i in range(b):
        letters.write('*')
    letters.write('\n')
    letters.write('C:')
    for i in range(c):
        letters.write('*')
    letters.write('\n')
    letters.write('D:')
    for i in range(d):
        letters.write('*')
    letters.write('\n')
    letters.write('F:')
    for i in range(f):
        letters.write('*')
    
    
    
    


        
main()
