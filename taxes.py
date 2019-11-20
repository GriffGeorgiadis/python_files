#Griffin Georgiadis
#CS21, Assignment 5
#Create a program that asks for the value of the property the dispays the assemssment and property tax
#create main function
def main():
    actual_value = int(input("Enter the actual value: "))
#validation
    while actual_value < 0:
        print("Actual value must be >=0")
        actual_value = int(input("Enter the actual value: "))
#recall function
    show_property_tax(actual_value)



#create show_property_tax function
def show_property_tax(real):
    tax = real * .6
    tax = format(tax, ',.2f')
    print("Assessed value: $",tax)
    value = real * .6
    value = value/100 * .72
    value = format(value, ',.2f')
    print("Property tax: $", value)



#close main
main()
