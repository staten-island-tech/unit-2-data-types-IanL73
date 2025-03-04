# My project
money = 500
while True:
    chuck = input("would you like to withdraw?")
    if chuck == "exit" or chuck == "no":
        print("Goodbye!")
        break
    else:
        draw = int(input("How much withdraw, boy."))
        if draw > money:
            print("You don't have that much, boy.")
        else:
            money = money - draw
            print("You have $",money,"left in savings.")

""" # Ben's project
items = []
item = float(input("what price first item"))
while True:
    items.append(item)
    cont = input("is that all?")
    if cont == "yes" or cont == "Yes":
        total = sum(items)
        break
    else:
        item = float(input("What price next item?"))
if total >= 100:
    total = total * 0.9
else:
    total = total
print("Your total is",total,) """