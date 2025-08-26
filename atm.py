Password=1234
attempt=3
balance=1000
withdraw=0
#pin security verification
while attempts > 0:
    pin_input = input("Enter your pin: ")
    if pin_input.isdigit():
        if int(pin_input) == Password:
            print("Welcome")
            break
        else:
            attempts -= 1
            print(f"Wrong pin. You have {attempts} attempts left.")
    else:
        attempts -= 1
        print(f"Invalid input. You have {attempts} attempts left.")
else:
    print("Too many wrong attempts. Exiting.")
    exit()
#the main interface
while True:
    print("ATM Menu")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change pin")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
#balance check
    if choice == 1:
        print("Your balance is: ",balance)
#To deposit money
    elif choice == 2:
        deposit = int(input("Enter the deposit amount: "))
        if deposit <= 0:
            print("Invalid deposit amount. Must be greater than 0.")
        else:
            balance += deposit
            print("Deposit successful. New balance is:", balance)
#To withdraw money    
    elif choice == 3:
        new_withdrawal=int(input("Withdraw amount"))
        if (new_withdrawal<=0):
            print(new_withdrawal,"is less than 0,Please try again.")
        elif(new_withdrawal>balance):
            print(" insuffecient balance")
        else:
            balance-= new_withdrawal
            print("Withdrawal successful. New balance:",balance)
#Changing password
    elif choice == 4:
        old_pin= int(input("enter the old password:"))
        if (old_pin== Password):
            new_pin= int(input("Enter new password:"))
            Password=new_pin
            print("Pin changed successfully.")
        else:
            print("Wrong pin. Try again.")
#final exit
    elif choice ==5:
        print("Thank you.")
        break
#Invalid user input   
    elif choice > 5:
        print("invalid entry.")

   