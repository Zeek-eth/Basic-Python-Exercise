from datetime import date
today = date.today()
date = today.strftime("%d.%m.%Y")
clients_name = "Test Person"
year = 1982
balance = 1698
print(f"{clients_name} {year}, balance: {balance} €, updated on {date}")