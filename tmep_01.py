#Griffin Geogiadis
#CS21
#This program converts celsius into fahrenheit
#get input from user
celsius = float(input('Enter Celsius temperature: '))

#calculate fahrenheit
#fahrenheit = (celsius * (9/5)) + 32

#print temperature in fahrenheit
#print('Fahrenheit temperature is', format(fahrenheit, '.2f')) 

#example
#for loops to print temperatures
for x in range (-40, 101, 20):
    fahrenheit = (x * (9/5)) + 32
    print (x, fahrenheit, sep='    ')
