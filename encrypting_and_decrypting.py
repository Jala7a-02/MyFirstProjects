import random
import string
char = string.punctuation + string.ascii_letters + string.digits + " "
char_list = list(char)
key = char_list.copy( )
random.shuffle(key)

# ENCRYPTING :

plain_text = input("please enter the message you like to encrypt .... :")
cipher_text = ""

for letter in plain_text :
    index = char.index(letter)
    cipher_text += key[index]

print(f"original text is : {plain_text}")
print(f"encrypted text is : {cipher_text}")



# DECRYPTING :

cipher_text = input("please enter the message you like to decrypt .... :")
plain_text = ""

for letter in cipher_text :
    index = key.index(letter)
    plain_text += char[index]
print(f"encrypted text is : {cipher_text}")
print(f"original text is : {plain_text}")
