import random

def print_is_prime():
    ranNums = 10
    for num in range(1, ranNums):
        if (ranNums % num) == 0:
            print(num,": Composite")
        else:
            print(num,": Prime")

print_is_prime()
        
