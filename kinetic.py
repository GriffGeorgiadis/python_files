#Griffin Georgiadis
#CS21
#write a program that gets an objects mass and velocity
def main():
    try:
        mass = int(input("Enter objects mass in grams here: "))
        vel = int(input("Enter objects velocity in seconds here: "))
        print("The Kinetic Energy is: ", kenetic_energy(mass, vel))
        #exceptions go here
    except ValueError:
        print("Invalid")
        print("Mass and velocity must be a number")
        

#calculate here
def kenetic_energy(mass, vel):
    KE = .5*mass*(vel)**2
    return KE

#call main
main()
