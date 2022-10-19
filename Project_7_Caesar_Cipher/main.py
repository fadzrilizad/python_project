import alphabet
import art

# print art
print(art.logo)

# caesar cipher function
def caesar(plain_text, shift_amount, cipher_direction):
    text = ""
    # if user_direction decode, minus shift amount 
    if cipher_direction == "decode":
        shift_amount *= -1
    
    # check character, alphabet or not 
    for char in plain_text:
        if char in alphabet.alphabet:
            # encode/decode text to new position
            position = alphabet.alphabet.index(char)
            new_position = position + shift_amount
            text += alphabet.alphabet[new_position]
        else:
            text += char

    # return result 
    return f"Here'r the {cipher_direction}d result: {text}"

# bool to end cipher 
end_cihper = False

# run cipher while true
while not end_cihper:
    # user input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Shift amount:\n"))
    # make sure shift not out of range
    shift = shift % 26
    # run function
    print(caesar(text, shift, direction))

    # restart cipher if user want to try again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if restart == "no":
        end_cihper = True
