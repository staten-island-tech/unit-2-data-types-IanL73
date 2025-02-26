""" glish = input("english text: ")
fren = input("french text: ") """

tcount = 0
scount = 0
x = input("WOOOOOOOOOOOORDS: ")
for i in x:
    if i == "t" or i == "T":
        tcount = tcount + 1
    else:
        tcount = tcount + 0
    if i == "s" or i == "S":
        scount = scount + 1
    else:
        scount = scount + 0
if scount >= tcount:
    print("This text is french, dude.")
else:
    print("This text is English.")