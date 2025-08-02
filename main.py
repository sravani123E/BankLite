from bank import Bank

def menu():
    print("\n=== BankLite – Console Banking System ===")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Balance")
    print("5. View Transaction History")
    print("6. Save Data")
    print("7. Load Data")
    print("0. Exit")

def main():
    bank = Bank()
    bank.load_from_file()

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter your name: ").strip()
                initial = float(input("Enter initial deposit: "))
                account = bank.create_account(name, initial)
                print(f"Account created with ID: {account.id}")

            elif choice == "2":
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter amount to deposit: "))
                bank.deposit_to_account(acc_id, amount)
                print("Amount deposited successfully.")

            elif choice == "3":
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw_from_account(acc_id, amount)
                print("Amount withdrawn successfully.")

            elif choice == "4":
                acc_id = int(input("Enter account ID: "))
                details = bank.show_account_details(acc_id)
                print(f"Balance for {details['Name']} (ID: {details['ID']}): ₹{details['Balance']}")

            elif choice == "5":
                acc_id = int(input("Enter account ID: "))
                details = bank.show_account_details(acc_id)
                print(f"Transaction history for {details['Name']}:")
                for t in details["History"]:
                    print("  -", t)

            elif choice == "6":
                bank.save_to_file()
                print("Data saved to bank.json.")

            elif choice == "7":
                bank.load_from_file()
                print("Data loaded from bank.json.")

            elif choice == "0":
                bank.save_to_file()
                print("Exiting. Data saved.")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
