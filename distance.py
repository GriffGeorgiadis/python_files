#Griffin Georgiadis
#CS21, Assignment 5
#Create a program than calculates the distance of an object when given the speed and time
#ask user for speed and time


speed = int(input("Enter the speed of the vehicle in mph: "))
#validate speed
while speed < 1:
    print("speed must be greater than zero")
    speed = int(input("Enter the speed of the vehicle in mph: "))

    

time = int(input("Enter the number of hours traveled: "))
#validatetime
while time < 1:
    print("time must be greater than zero")
    time = int(input("Enter the number of hours traveled: "))
    
#create table headings
print("Hours\tDistance Traveled")
print("------------------------")
#create loop
for num in range(1, time +1):
    total = num * speed
    print(num, format(total, '10,.1f'))

        
xx
