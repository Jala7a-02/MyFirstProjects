def show_balance():
    print(f"Your balance is : ${balance:.2f}")
def deposite():
    amount = float(input(f"Please inter the amount you like to deposit "))
    if amount < 0 :
        print("that's not valid")
        return 0
    else :
        return amount
    
def withdraw():
    
    amount = float(input(f"Please inter the amount you like to witdraw "))
    if amount < 0 :
        print("that's not valid")
        return 0
    elif amount > balance :
        print(f"you don't have a sufficient balane to withdraw {amount}")
        return 0
    else :
        return amount
def main():
    global balance
    balance = 0
    is_running = True

    while is_running :
        print("Welcome to Banking programming")
        print("1 - Show Balance\n2 - Deposite\n3 - withdraw\n4 - Exit")
        choice = input("please select your process(1-4) ")
        if choice == "1" :
            show_balance()
        elif choice == "2" :
            balance += deposite()
        elif choice == "3" :
            balance -= withdraw()
        elif choice == "4":
            is_running = False
        else :
            print("that's not a valid choice")

    print("Thank you , have a nice day")
if __name__ == "__main__" :
    main()