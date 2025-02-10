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

""" # Now it's time for the madlibs project. yeehaw.
name = input("Give me a name. It doesn't have to be yours, just anyone you think is interesting.")
verb1 = input("Give me a verb.")
adjective1 = input("Give me an adjective.")
verb2 = input("Give me another verb.")
noun1 = input("Give me a noun.")
adjective2 = input("Give me another adjective.")
numeral = input("Give me a number in writen form. Like, one not 1.")
verb3 = input("Give me a third verb.")
noun2 = input("Give me another noun.")
adjective3 = input("Give me a third adjective.")
guest = input("Give me a famous person. They don't have to be real, they just need to be popular.")
verb4 = input("Give me a fourth verb, I promist the is the last one.")
# put more things here if you need them, kay ;3

# okay so the story's going to sound like this:
#  Once upon a time, there lived one "(instert name)". (Instert Name) was taking nice stroll through the fields, enjoying their time to the fullest. After taking a spell to (verb1), they set their sights on a(n) (adjective1), yet inviting woods. upon walking in, they find themself transported to a world of wonder, filled with whimsical creatures, (verb2)ing (noun1)s, and magic glowing lights of no discernable origin. (Name) begins to wander, taking in all the sights, smells, and sounds of the forest, leaving them completely vulnerable, and oblivious, to the dangers that lurk just out of sight. Suddenly, (Name) is a attacked by a ferocious pack of (numeral), (adjective2), (verb3)ing (noun2)s!! Oh! The horror! Just as (name) is coming to terms with their untimly and, frankly, unceremonious demise, a miracle occurs! (guest) appears from the brush, striking down each and every (noun2) with grace and skill. (guest) helps (name) up and, after making sure they're okay, walks home with them, the two (verb4)ing all the way. The End.
print("Once upon a time, there lived one",name+".",name,"was taking nice stroll through the fields, enjoying their time to the fullest. After taking a spell to",verb1+", they set their sights on a(n)",adjective1+", yet inviting woods. Upon walking in, they find themself transported to a world of wonder, filled with whimsical creatures,",verb2+"ing",noun1+"s, and magic glowing lights of no discernable origin.",name,"begins to wander, taking in all the sights, sounds, and smells of the forest, leaving them completely oblivious to the dangers lurking just out of sight. Suddenly,",name,"is attacked by a ferocious pack of",numeral+",",verb3+"ing",noun2+"s! Oh! The horror! Just as",name,"is coming to terms with their untimely and, frankly, quite unceremonious demise, a miracle occurs!",guest,"appears from the brush!, striking down each and every",noun2,"with the grace of a butterfly, and cruel precision of a... a uh... like, some kind of... precision, animal. Or something. Anyway,",guest,"helps",name,"up and, after making sure they're okay, walks home with them, the two,",verb4+"ing all the way. The End.") """

""" #intro to bouillon. I love soup.
day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

#F string
x = "bees"
print(f"hello {x}")