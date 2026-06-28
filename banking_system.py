from datetime import datetime


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner}: P{self.balance:.2f}"


class Transaction:
    def __init__(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()

    def execute(self, account):
        raise NotImplementedError("Child class must implement execute()")

    def get_type(self):
        return "Transaction"

    def summary(self):
        return f"[{self.get_type()}] {self.description}: P{self.amount:.2f} at {self.timestamp:%H:%M:%S}"


class Deposit(Transaction):
    def __init__(self, amount, description="Deposit", source="counter"):
        super().__init__(amount, description)
        self.source = source

    def execute(self, account, apply_interest=False):
        if apply_interest:
            interest = self.amount * 0.015
            account.balance += self.amount + interest
            print(f"  -> Deposited P{self.amount:.2f} + P{interest:.2f} interest")
        else:
            account.balance += self.amount
            print(f"  -> Deposited P{self.amount:.2f}")

    def get_type(self):
        return "Deposit"


class Withdrawal(Transaction):
    def __init__(self, amount, description="Withdrawal", fee=0):
        super().__init__(amount, description)
        self.fee = fee

    def execute(self, account, waive_fee=False):
        total = self.amount
        if not waive_fee:
            total += self.fee
        if account.balance < total:
            print(f"  -> Insufficient balance! Need P{total:.2f}, have P{account.balance:.2f}")
            return False
        account.balance -= total
        print(f"  -> Withdrew P{self.amount:.2f}", end="")
        if self.fee and not waive_fee:
            print(f" (fee P{self.fee:.2f})", end="")
        print()
        return True

    def get_type(self):
        return "Withdrawal"


class Transfer(Transaction):
    def __init__(self, amount, description="Transfer", recipient=None):
        super().__init__(amount, description)
        self.recipient = recipient

    def execute(self, account, express=False):
        fee = 5 if express else 15
        total = self.amount + fee
        if account.balance < total:
            print(f"  -> Insufficient balance! Need P{total:.2f}, have P{account.balance:.2f}")
            return False
        account.balance -= total
        if self.recipient:
            self.recipient.balance += self.amount
        print(f"  -> Transferred P{self.amount:.2f} to {self.recipient.owner if self.recipient else 'unknown'}"
              f" (fee P{fee:.2f})")
        return True

    def get_type(self):
        return "Transfer"


if __name__ == "__main__":
    print("=" * 50)
    print("  BANKING SYSTEM — Method Overloading & Overriding")
    print("=" * 50)

    employer = Account("Employer", 5000)
    employee = Account("Employee", 500)

    print(f"\nStart balances:  {employer}  |  {employee}")
    print("-" * 50)

    print("\n1. Employer deposits P1500 (standard):")
    d1 = Deposit(1500, "Monthly revenue")
    d1.execute(employer)
    print(f"   New balance: {employer}")

    print("\n2. Employer deposits P2000 with interest (apply_interest=True):")
    d2 = Deposit(2000, "Investment deposit")
    d2.execute(employer, apply_interest=True)
    print(f"   New balance: {employer}")

    print("\n3. Employer withdraws P1000 (with fee):")
    w1 = Withdrawal(1000, "ATM withdraw", fee=10)
    w1.execute(employer)
    print(f"   New balance: {employer}")

    print("\n4. Employer withdraws P500 with fee waived (waive_fee=True):")
    w2 = Withdrawal(500, "Preferred withdrawal", fee=10)
    w2.execute(employer, waive_fee=True)
    print(f"   New balance: {employer}")

    print("\n5. Employer transfers P800 to Employee (standard):")
    t1 = Transfer(800, "Payroll transfer", recipient=employee)
    t1.execute(employer)
    print(f"   Balances:  {employer}  |  {employee}")

    print("\n6. Employer transfers P300 to Employee (express=True, lower fee):")
    t2 = Transfer(300, "Bonus transfer", recipient=employee)
    t2.execute(employer, express=True)
    print(f"   Balances:  {employer}  |  {employee}")

    print("\n" + "=" * 50)
    print("  TRANSACTION LOG (polymorphism in action):")
    print("=" * 50)
    for t in [d1, d2, w1, w2, t1, t2]:
        print(f"  {t.summary()}")

    print(f"\nFinal balances:  {employer}  |  {employee}")
