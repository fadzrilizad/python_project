import random # random module

# list letters, number & symbols
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Print message
print("Welcome to the password generator")
input_words = int(input("How many words would you like in your password?\n"))
input_numbers = int(input("How many numbers would you like in your password?\n"))
input_symbols = int(input("How many symbols would you like in your password?\n"))

# passGenerator function
def passGenerator(input_words, input_numbers, input_symbols):
    # save paswords in list
    password = []

    # generate random letters
    for char in range(0, input_words):
        password += random.choice(letters)

    # generate random numbers
    for char in range(0, input_symbols):
        password += random.choice(numbers)

    # generate random symbols
    for char in range(0, input_symbols):
        password += random.choice(symbols)

    # random list
    random.shuffle(password)

    # loop list to print in variable
    printCharacter = ""

    for char in password:
        printCharacter += char

    return printCharacter


print(passGenerator(input_words, input_numbers, input_symbols))
