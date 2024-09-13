import random

s=input("Enter the String ")

if(s):
    random_char= random.choice(s)
    print(f"Randomly picked character is {random_char}")
else:
    print("Nothing to print")