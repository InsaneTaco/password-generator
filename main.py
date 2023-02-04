import random as r

#defines each type of item
low_letters = ("abcdefghijklmnopqrstuvwxyz")
upper_letters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = ("012345679")
special_ch = ("!@#$%^&?/-_=+:'")
character_types = [low_letters]

output = "" # blank output

# gets user input on what types of characters will be in the password
print("How many characters long do you want your password? Enter any whole number.")
ch_count = int(input())

# lowercase/mixed
print("\nShould the password be 'lowercase' or 'mixed'?")
case_type = input().lower()
if case_type == "mixed":
    character_types.append(upper_letters)

# numbers
print("\nDo you want there to be numbers? 'yes'/'no'")
has_numbers = input().lower()
if has_numbers == "yes":
    character_types.append(numbers)

# special symbols/characters
print("\nDo you want there to be special symbols/characters? 'yes'/'no'")
has_special_ch = input().lower()
if has_special_ch == "yes":
    character_types.append(special_ch)

# picks one of the character types randomly to put into the password
for i in range(ch_count):
    selected_list = r.choice(character_types)
    output += r.choice(selected_list)

print("\nGenerating...")
print(output)