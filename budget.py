#Griffin Georgiadis
#CS21, Assignment 4
#Write a progrma where the user gives there expenses for the month and at the end att up to see if she is over or under budget
#enter the budget for the month
budg = float(input("Enter amount budgeted for the month: "))
format(budg, '.2f')
spent = 1

#input expenses
total = 0
while spent > 0:
    spent = float(input("Enter an amount spent(0 to quit): ", ))
    total = total + spent
#display budget, spent, if you were over or under
print("Budgeted: $", format(budg, '.2f'))
print('Spent: $', format(total, '.2f'))

left = budg - total
over = total - budg

if total < budg:
    print('You are $', format(left, '.2f'), 'under budget. WELL DONE!')
else:
    print('You are $', format(over, '.2f'),'over budget. PLAN BETTER NEXT TIME!')

    
    
    
