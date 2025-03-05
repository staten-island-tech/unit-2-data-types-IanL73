# Ben's project
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
print("Your total is",total,)