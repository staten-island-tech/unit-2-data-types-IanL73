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