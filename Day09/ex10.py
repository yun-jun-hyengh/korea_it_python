class Account:
    def __init__(self, owner, balance):
        self.owner = owner;
        self.balance = balance;

    def deposit(self, amount):
        self.balance = self.balance + amount;

    def show_balance(self):
        print(f"잔액: {self.balance}원")

acc = Account("김철수", 10000);
acc.show_balance();
acc.deposit(110000);
acc.show_balance();