print("=== ATM BANKING SYSTEM ===")
print("1. Create Account")
print("2. Check Balance")
print("3. Deposit Money")
print("4. Withdraw Money")
print("5. Transfer Money")
print("6. Transaction History")
print("7. Exit")

accounts = {}
transactions = []

while True:
    choose = int(input("Enter your choice : "))
    print("Your choice is :", choose)

    if choose == 1:
        account_number = input("Enter account number with 4 numbers : ")
        name = input("Enter account name : ")
        pin = input("Create a PIN with 4 numbers : ")

        accounts[account_number] = {
            "name": name,
            "pin": pin,
            "balance": 0
        }

        print("Account created successfully..")

    elif choose == 2:
        account_number = input("Enter your 4 digit account number : ")

        if account_number in accounts:
            pin = input("Enter your PIN : ")

            if pin == accounts[account_number]["pin"]:
                print("Account holder :", accounts[account_number]["name"])
                print("Your bank balance : ₹", accounts[account_number]["balance"])
            else:
                print("Incorrect PIN..")
        else:
            print("Account not found..")

    elif choose == 3:
        account_number = input("Enter your 4 digit account number : ")

        if account_number in accounts:
            pin = input("Enter your PIN : ")

            if pin == accounts[account_number]["pin"]:
                amount = float(input("Enter amount to deposit : "))

                if amount > 0:
                    accounts[account_number]["balance"] += amount

                    transactions.append(
                        f"Deposit: ₹{amount} to account {account_number}"
                    )

                    print("Amount deposited successfully..")
                    print("Your new balance : ₹", accounts[account_number]["balance"])
                else:
                    print("Enter a valid amount..")
            else:
                print("Incorrect PIN..")
        else:
            print("Account not found..")

    elif choose == 4:
        account_number = input("Enter your 4 digit account number : ")

        if account_number in accounts:
            pin = input("Enter your PIN : ")

            if pin == accounts[account_number]["pin"]:
                amount = float(input("Enter withdrawal amount : "))

                if amount <= 0:
                    print("Enter a valid amount..")

                elif amount > accounts[account_number]["balance"]:
                    print("Insufficient balance..")

                else:
                    accounts[account_number]["balance"] -= amount

                    transactions.append(
                        f"Withdrawal: ₹{amount} from account {account_number}"
                    )

                    print("Amount withdrawn successfully..")
                    print("Your new balance : ₹",
                          accounts[account_number]["balance"])
            else:
                print("Incorrect PIN..")
        else:
            print("Account not found..")

    elif choose == 5:
        sender_account = input("Enter your account number : ")

        if sender_account in accounts:
            pin = input("Enter your PIN : ")

            if pin == accounts[sender_account]["pin"]:

                receiver_account = input("Enter receiver account number : ")

                if receiver_account in accounts:
                    amount = float(input("Enter amount to transfer : "))

                    if amount <= 0:
                        print("Please enter a valid amount..")

                    elif amount > accounts[sender_account]["balance"]:
                        print("Insufficient balance..")

                    else:
                        accounts[sender_account]["balance"] -= amount
                        accounts[receiver_account]["balance"] += amount

                        transactions.append(
                            f"Transfer: ₹{amount} from "
                            f"{sender_account} to {receiver_account}"
                        )

                        print("Money transferred successfully..")
                        print("Your new balance : ₹",
                              accounts[sender_account]["balance"])

                else:
                    print("Receiver account not found..")

            else:
                print("Incorrect PIN..")

        else:
            print("Your account not found..")

    elif choose == 6:
        account_number = input("Enter your account number : ")

        if account_number in accounts:
            pin = input("Enter your PIN : ")

            if pin == accounts[account_number]["pin"]:
                print("\n=== TRANSACTION HISTORY ===")

                if transactions:
                    for transaction in transactions:
                        print(transaction)
                        print("----------------")
                else:
                    print("No transactions found..")
            else:
                print("Incorrect PIN..")
        else:
            print("Account not found..")

    elif choose == 7:
        print("Thank you for using our ATM banking system..")
        break

    else:
        print("Invalid choice.. Please choose between 1 and 7.")