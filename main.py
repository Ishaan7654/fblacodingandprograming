from financemanager import FinanceManager


ramin = FinanceManager("Ramin")

print(ramin.balance)
ramin.add_to_balance(100)
print(ramin.balance)