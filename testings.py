##def main():
##
##
## try:
## # Get mass
##     mass = float(input("Enter the mass of the object in kilograms: "))
##
## # Get velocity
##     velocity = float(input("Enter object velocity in meters per second: "))
##
## # Get kinetic energy
##     ke = kinetic_energy(mass, velocity)
##
## # Show Kinetic Energy
##     print ("Kinetic Energy is: ", format(ke, '.2f'), "joules")
## except ValueError:
##     print('Error in input. No calculations performed.')
##
## # The kinetic_energy function receives the mass and velocity of
## # an object and returns its kinetic energy
##def kinetic_energy(mass, velocity):
##
##    ke = (mass * velocity * velocity) / 2
##    return ke
##
##main()
def main():
    
    one = 1
    two = 1
    three = 1
    smallest(one,two,three)
 
def smallest(one,two,three):
    if one == two == three:
        print('true')
    else:
        print('false')
main()
