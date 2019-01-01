from math import floor


def change_calculator():
    price = float(input("Please input the price of the item"))
    money = float(input("Please input how much cash you're paying"))
    if price < money:
        change = money - price
        print('Your change is $', change)
        coin_calculator(change)
        end()
    else:
        print("You're not paying enough for the item")
        change_calculator()


def coin_calculator(change):
    coins = {'dollar': 1.0, 'quarter': 0.25, 'dime': 0.1, 'nickel': 0.05, 'penny': 0.01}
    for coin, value in coins.items():
        temp = floor(change / value - change % value)
        print('your change is', temp, coin,'(s)')
        change = change - temp * value
        if change <= 0:
            break


def end():
    response = input("Would you like to try again?")
    if response == "Yes":
        change_calculator()
    else:
        print('Thanks!')


print("Welcome to Change Calculator!")
print('')
change_calculator()
