""" x = 3   # the difference between integers and floats in python
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15] # this is a list. It contains numbers. Obviously. Important to note, it does not discriminate between Integers and Floats. Pretty Handy. """
""" print(values) # using "print" on the name of the list prints the whole list (brackets included).
for i in values: # this prints every value in it's own line.
    print(i) """

""" print(values[6]) # this function lets you print various values individually. Remember that CS starts counting at 0. """

# Strings! Strings hold "text" values. Strings aren't "just text", each word is actually a list consisting of each letter in it.
# for example, "test" is ["t","e","s","t"]
""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" sent = input("Give me a sentence") # this function takes a sentence and tells you how many words are in it I'm very proud of it :3
wordlist = sent.split( )
wordnumber = 0
for i in wordlist:
    wordnumber = wordnumber + 1
print(wordnumber) """

# Now it's time for the madlibs project. yeehaw.
verb1 = input("Give me a verb.")
verb2 = input("Give me another")
noun = input("Give me a noun.")
numeral = input("Give me a number in writen form. Like, one not 1.")
guest = input("Lastly, give me a famous person. They don't have to be real, they just need to be popular.")
# put more things here if you need them, kay ;3
