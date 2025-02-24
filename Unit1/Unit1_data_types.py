 # THESE ARE VERY IMPORTANT!! MEMORISE!!

# strings represent characters, names, and words
name = "Kammy"

# integers for WHOLE numbers
age = 76 #lmao

# a Boolean is a true or false, typically used for evaluations.
graduated = False
    #i.e. 
    # if "tall" then "leg sweep for increased damage"

# Floats for decimals\
money = 5.23

# Input! put in input, outputs as variable
#defaults to string. See above.

bill = input("how much was the bill")
#this will not work

#try this instead!

bill = int(input("how much was the bill")) # this will turn the data type into an integer
# it probably should be a float considering we're dealing with money, but I digress """

# we have lists too
students = ["kammy", "Rachel", "Denis", "Ben"]
# similar to for i in range(4)
for student in students:
    print(student)