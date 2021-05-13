print("PRATYUSH AVI A203")
select = input("1. Encryption or 2. Decryption (1/2):")

if select == "1":
    text = input("Enter your Plain text message: ")
    letters = "abcdefghijklmnopqrstuvwxyz "
    Key     = "kryptosabcdefghijlmnquvwxz "


    new_string = ""
    cipher_text = []

    for char in text:
        if char in letters:
            new_string += char

    def encrypt():
        index_values = [letters.index(char) for char in new_string]
        return "".join(Key[indexKey] for indexKey in index_values)

    encrypted_message = encrypt()
    print("The encrypted message is:" +encrypted_message)

elif select == "2":
    text = input("Enter your Plain text message: ")
    letters = "kryptosabcdefghijlmnquvwxz "
    Key     = "abcdefghijklmnopqrstuvwxyz "

    new_string = ""
    cipher_text = []

    for char in text:
        if char in letters:
            new_string += char

    def decrypt():
        index_values = [letters.index(char) for char in new_string]
        return "".join(Key[indexKey] for indexKey in index_values)

    decrypted_message = decrypt()
    print("The decrypted message is:" +decrypted_message)

elif select != "1" or select != "2":
    print("Choose from the above option")
