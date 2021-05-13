import string
print("PRATYUSH AVI")
select = input("1. Encryption or 2. Decryption (1/2):")

if select == "1":
    text=input("Enter the text: ")
    key=input("Enter the Key: ")
    cipher=""
    index=0
    for c in text:
        if c in string.ascii_lowercase:
            offset=ord(key[index])-ord('a')

            encryption=chr((ord(c) - ord('a') + offset) % 26 + ord('a'))
            cipher=cipher + encryption

            index=(index + 1) % len(key)
        else:
            cipher=cipher + c

    print("The key is:"+ key)
    print("The Input Text is: "+ text)
    print("The Encryption Cipher is: "+ cipher)

elif select == "2":
    text=""
    key=input("Enter the Key: ")
    cipher=input("Enter the text: ")
    index=0
    for c in cipher:
        if c in string.ascii_lowercase:
            offset=ord(key[index])-ord('a')
            decryption=ord(c) - ord('a') - offset
            if decryption<0:
                decryption=decryption + 26
            decrypt=chr(decryption + ord('a'))

            text=text + decrypt

            index=(index + 1) % len(key)
        else:
            text=text + c

    print("The Decryption text is: "+ text)

elif select !="1" or select !="2":
    print("Choose from the above option")

