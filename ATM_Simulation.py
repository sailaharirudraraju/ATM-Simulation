def show_menu():
    print("1.Check_balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

balance=10000
def check_balance(balance):
    print("Balance:",balance)

def deposit(balance):
    amount=int(input("Enter amount:"))
    if amount<=0:
        print("Transaction rejected")
        return balance
    balance+=amount
    print("Balance after deposit:",balance)
    return balance
    
def withdraw(balance):
    amount=int(input("enter amount:"))
    if balance<amount:
        print("Insufficent Balance")
    elif amount<=0:
        print("Rejected transaction")
    else:
        balance=balance-amount
        print("Remaining balance:",balance)
    return balance
while True:
    show_menu()
    choice=int(input("enter your choice:"))
    if choice==1:
        check_balance(balance)
    elif choice==2:
        balance=deposit(balance)
    
    elif choice==3:
        balance=withdraw(balance)
        
    elif choice==4:
        print("Exited")
        break
    else:
        print("Please enter valid choice")

