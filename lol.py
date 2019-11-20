#Griffin Georgiadis
#CS21, Assignment 4 pt.2
#To display the predicted population of the US in a specfic number of years
#Calculate number of death vs births vs immagrans
births = 3942000
deaths = 2866909
imm = 1051200
pop = 320387104

#calculate your prediction

print('The current population is 320,387,104 in year 2015')
years = int(input('How many years out would you like to predict? '))
final_years = 2015

if years < 0:
    print('Value must be positive')
    years = int(input('How many years out would you like to predict? '))
    
   
#display in a table


for total in range(1, years + 1):
        final = (total)*((births+imm)-deaths)+pop
        print(total + final_years, final, sep='  ')

#Validation10

while years < 0:
    print("Error years must be more that zero!!")
    
