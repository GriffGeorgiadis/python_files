#Griffin Georgiadis
#CS21
#This program will take the number of seconds you input and covert it into
#days, hours, minuets and seconds
#Have user input number of seconds
secs = int(input('Enter the number of seconds: ', ))
#calculate conversons
days = secs // 86400

hours = (secs // 3600) % 24

mins = (secs // 60) % 60

seconds = secs % 60


#Calculate if seconds will be converted into days, hours, ect..
if secs > 0:
    if secs < 60:
           print(secs, "seconds =", days, "days", hours, "hours", mins, "minutes,", seconds, "seconds")
    elif secs >= 60 and secs < 3600:
           print(secs, "seconds =", days, "days", hours, "hours", mins, "minutes,", seconds, "seconds")
    elif secs >= 3600 and secs < 86400:
           print(secs, "seconds =", days, "days", hours, "hours", mins, "minutes,", seconds, "seconds")
    else:
        secs >= 86400;
        print(secs, "seconds =", days, "days", hours, "hours", mins, "minutes,", seconds, "seconds")

           
#if negative value print error
else:
    secs <= 0;
    print("Seconds must be a value >= 0")


