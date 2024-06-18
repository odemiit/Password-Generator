#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#get a random letter from the list "letters" for how many letters wanted and append it to the letters section of the password
# pass_letters = ""
# for letter in range(1, nr_letters + 1):
#   letter = random.choice(letters)
#   pass_letters += letter

#get a random letter from the list "letters" for how many symbols wanted and append it to the symbols section of the password
# pass_symbols = ""
# for symbol in range(1, nr_symbols + 1):
#     symbol = random.choice(symbols)
#     pass_symbols += symbol

#get a random number from the list "letters" for how many letters wanted and append it to the numbers section of the password
# pass_numbers = ""
# for number in range(1, nr_numbers + 1):
#       number = random.choice(numbers)
#       pass_numbers += number

#combine all the generated sections in one string
# total_password = pass_letters + pass_symbols + pass_numbers

#print out password
# print(f"Here is your password: {total_password}")

#Hard Level - Order of characters randomized:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#get a random letter from the list "letters" for how many letters wanted and append it to the letters section of the password
pass_letters = []
for letter in range(1, nr_letters + 1):
  letter = random.choice(letters)
  pass_letters.append(letter)

#get a random letter from the list "letters" for how many symbols wanted and append it to the symbols section of the password
pass_symbols = []
for symbol in range(1, nr_symbols + 1):
    symbol = random.choice(symbols)
    pass_symbols.append(symbol)

#get a random number from the list "letters" for how many letters wanted and append it to the numbers section of the password
pass_numbers = []
for number in range(1, nr_numbers + 1):
      number = random.choice(numbers)
      pass_numbers.append(number)

#combine all the lists together
combined_chars = pass_letters + pass_symbols + pass_numbers

#randomly shuffle the characters in the list
combined_chars = random.sample(combined_chars, len(combined_chars))

#convert the list into a string
final_password = ""

for character in combined_chars:
  final_password += character

#print out final password
print(f"Here is your password: {final_password}")

