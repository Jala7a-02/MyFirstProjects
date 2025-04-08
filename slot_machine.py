import random 
def spin_row() :

    symbols = ["⭐", "🍉" ,"🍒", "🍋", "🔔"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row) :

    print("************")
    print(" | ".join(row))
    print("************")

def get_payout(row, bet) :

    if row[0] == row[1] == row[2] :
        if row[0] == "🍒" :
            return bet * 3
        elif row[0] == "🍉" :
            return bet * 4
        elif row[0] == "🍋" :
            return bet * 5
        elif row[0] == "🔔" :
            return bet * 6
        elif row[0] == "⭐" :
            return bet * 10
    return 0


def main() :
    balance = 100
    print("**************************")
    print("   Welcom to Python slots  ")
    print("symbols : ⭐ 🍉 🍒 🍋 🔔 ")
    print("***************************")

    while balance > 0 :
        print(f"your balance is : ${balance:.2f}")
        bet = input("plaese insert your bet")
        if not bet.isdigit() :
            print("please inter a valid number")
            continue
        bet = int(bet)
        
        if bet > balance :
            print("insufficient balance")
            continue
        if bet <= 0 :
            print("bet should be greater than zero")
            continue
        balance -= bet
        row = spin_row()
        print("spinning...\n")
        print_row(row)
        payout = get_payout(row, bet)
        balance += payout
        if payout > 0 :
            print(f"you have earned ${payout}")
        else :
            print("sorry you've lost this round")

        play = input("do you like to continue playing (y/n) ").lower()
        
        if play != "y" :

            break
    print("********************************")
    print(f"your new balance is : {balance}")
    print("Thanks for playing, Have a nice day")
    print("*****************************")

main()