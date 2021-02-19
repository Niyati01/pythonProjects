import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_lowercase)



def encrypt(message, shft):
    encryptstring = ""

    for m in message:
        if m in alphabet:
            encryptstring += alphabet[alphabet.index(m)+shft]
    print(encryptstring)       

def decrypt(message, shft):
    decryptstring = ""
    for m in message:
        if m in alphabet:
            decryptstring += alphabet[alphabet.index(m)-shft]
    print(decryptstring) 

direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")

text = input("\nType the message : ")
shift = int(input("\n Type the Shift number : "))

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
