#Gym_Membership is the constant
GYM_MEMBERSHIP = 100
#paid is the variable
paid = int(input("Please enter required amount: -"))
balance = Gym_Membership - paid

if balance == 0:
    print("Gym access granted")
elif balance > 0:
    print("Please settle your balance of " + str(balance) + " in order to access gym.")
elif balance < 0:
    print("Your change will be moved to next months membership ")
else:

    print("Error.")