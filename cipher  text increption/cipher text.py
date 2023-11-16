import os
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def clear_screen():
    os.system("cls")

def caeser(start_text , shift_amount , cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            possition = alphabet.index(char)
            new_possition = possition + shift_amount
            end_text += alphabet[new_possition]
        else:
            end_text += char
    print(f"the {cipher_direction}d text is '{end_text}'.")

print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt ,, Type 'decode' to decrypt \n >> ").lower()
    text = input("type your massage \n >> ").lower()
    shift = int(input("type the secret shift number \n >> "))
    
    shift = shift % 26 
    caeser(start_text= text, shift_amount= shift, cipher_direction= direction)

    restart = input("Type 'yes' if you want to go agian ,, otherwise type 'no' \n >> ").lower()
    if restart == "yes" :
        clear_screen()
        print(logo)
    if restart == "no" :
        clear_screen()
        should_end = True
        print("goodbye")




#   ...   in line 30 we added this code beacause if the user enter a number gretter than 26
#   ...   we will be able to track it so we remind it to 26 and the number we get we shift on it 
#   ...   >>>> TEST
#   ...   >> direction is encode
#   ...   >> text is hello
#   ...   >> shift is 5 
#   ...                  >> the output will be mjqqt 
#   ...   what if the user entered a number like 31
#   ...   so we remind it to 26 and the reminder will be the shift
#   ...   31 % 26 = 5
#   ...   what if the user entered a number like 187
#   ...   so we remind it to 26 and the reminder will be the shift
#   ...   187 % 26 = 5
#   ...                            ....and so on  <<
