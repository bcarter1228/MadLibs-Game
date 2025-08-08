print(" \nWelcome to my Mad Libs Game!")
message = """

The story will be a surprise. Just enter the words you \n want, and the program will reveal the story you've created \nwhen you've filled everything out. Hint: It's medical related!
"""
print(message)

word1 = input("Enter an Adjective: ")
word2 = input("Enter a Place: ")
word3 = input("Enter an Adjective: ")
word4 = input("Enter an Adjective: ")
word5 = input("Enter a Piece of Clothing: ")
word6 = input("Enter a Body Part: ")
word7 = input("Enter a Body Part: ")
word8 = input("Enter a Body Part: ")
word9 = input("Enter an Adjective: ")
word10 = input("Enter a Noun: ")
word11 = input("Enter a Noun: ")
word12 = input("Enter a Place: ")
word13 = input("Enter an Adjective: ")

print("\nHere's your story. Hope you enjoy!")
story_formatted = f"""\nEvery year, you should visit 
a doctor. It is a very {word1} visit. Usually, you 
have to skip going to {word2} to go. Your doctor is 
usually a {word3} person who is wearing a {word4} {word5}. 
They will look at your {word6}, {word7}, and {word8}. 
Sometimes, they can be very {word9}. Afterwards, they 
will give you a {word10} and a {word11} and your dad's 
mistress will take you to {word12} as a treat. All in all, 
the doctor's office isn't so {word13}!"""
print(story_formatted)
