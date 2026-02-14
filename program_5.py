# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    budget=float(input("Enter your budget: ")) #User enter Budget
    total_expenses= 0.0
    while True:
        expenses = float(input("Enter your expenses( or 0 to finsh): ")) #User enter expenses
        if expenses == 0:
            break #Stops loop when 0 is entered
        total_expenses += expenses
    difference= total_expenses - budget
    if difference > 0:
        print(f" You are over budget by ${difference:.2f}.")  #Tells user if over budget
    elif difference < 0:
        print(f" You are under budget by ${abs(difference):.2f}"" Congrats") #Tells user if under budget
    else:
        print("You are exactly on budget" " Be careful") #Tells user when still on budget
    ######################


if __name__ == '__main__':
    main()
