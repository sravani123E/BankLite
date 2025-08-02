import json
from account import Account

class Bank:
    def __init__(self):
        self.accounts = []
        self.next_id = 1

    def create_account(self, name, initial_balance=0.0):
        account = Account(self.next_id, name, initial_balance)
        self.accounts.append(account)
        self.next_id += 1
        return account

    def find_account_by_id(self, account_id):
        for acc in self.accounts:
            if acc.id == account_id:
                return acc
        return None

    def deposit_to_account(self, account_id, amount):
        account = self.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found.")
        account.deposit(amount)

    def withdraw_from_account(self, account_id, amount):
        account = self.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found.")
        account.withdraw(amount)

    def show_account_details(self, account_id):
        account = self.find_account_by_id(account_id)
        if not account:
            raise ValueError("Account not found.")
        return {
            "ID": account.id,
            "Name": account.name,
            "Balance": account.get_balance(),
            "History": account.get_history()
        }

    def save_to_file(self, filename="bank.json"):
        with open(filename, "w") as f:
            json.dump([acc.to_dict() for acc in self.accounts], f, indent=4)

    def load_from_file(self, filename="bank.json"):
        try:
            with open(filename, "r") as f:
                content = f.read().strip()
                if not content:
                    # Empty file, treat as no accounts
                    self.accounts = []
                    return
                try:
                    data = json.loads(content)
                except json.JSONDecodeError:
                    # Invalid JSON, treat as no accounts
                    self.accounts = []
                    return
                self.accounts = [Account.from_dict(acc_data) for acc_data in data]
                if self.accounts:
                    self.next_id = max(acc.id for acc in self.accounts) + 1
        except FileNotFoundError:
            self.accounts = []
