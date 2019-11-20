#Griffin Georgiadis
#CS21, Assignment 7
#Write a program that allows you to call a file
def main():
    try:
        sampleprogram = open('sampleprogram.py','w')
        sampleprogram.write('#Griffin Georgiadis\n')
        sampleprogram.write('#CS21\n')
        sampleprogram.write('#Sample program\n')
        sampleprogram.write('\n')
        sampleprogram.write('print("This is a sample program")\n')
        sampleprogram.write('print("Remember when this was hard?")\n')
        sampleprogram.write('print("Python is cool")\n')
    except IOError:
        sampleprogram.close()
        ssampleprogram = open('ln_sampleprogram.py','w')
        sampleprogram = open('sampleprogram.py','r')
        line1 = sampleprogram.readline()
        line2 = sampleprogram.readline()
        line3 = sampleprogram.readline()
        line4 = sampleprogram.readline()
        line5 = sampleprogram.readline()
        line6 = sampleprogram.readline()
        line7 = sampleprogram.readline()

        ssampleprogram.write('1: ')
        ssampleprogram.write(line1)
        ssampleprogram.write('2: ')
        ssampleprogram.write(line2)
        ssampleprogram.write('3: ')
        ssampleprogram.write(line3)
        ssampleprogram.write('4: ')
        ssampleprogram.write(line4)
        ssampleprogram.write('5: ')
        ssampleprogram.write(line5)
        ssampleprogram.write('6: ')
        ssampleprogram.write(line6)
        ssampleprogram.write('7: ')
        ssampleprogram.write(line7)
        
        
    except IOError:
        sampleprogram.close()
        ssampleprogram.close()
        



main()

    


    
