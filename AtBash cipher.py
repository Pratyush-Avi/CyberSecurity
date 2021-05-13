print("PRATYUSH AVI A203")
select = input("1. Encryption or 2. Decryption (1/2):")

if select == "1":
    cipher = "" 
    word = input("Enter the text:")
    for char in word:
        encrypt = ord(char)
        if encrypt in range(65,91):
            result = encrypt - 65
            result = 25 - result
            encrypt = result + 65
            atbash = chr(encrypt)
            
        elif encrypt in range(97,123):
            result = encrypt - 97
            result = 25 - result
            encrypt = result + 97
            atbash = chr(encrypt)
        
        elif encrypt<65 or encrypt>90 or encrypt <97 or encrypt>122:
            atbash = chr(encrypt)
        cipher += atbash
        
    print("The result to decrypt is:"+cipher)
    
elif select == "2":
    formal = ""
    word = input("Enter the text:")
    for char in word:
        decrypt = ord(char)
        if decrypt in range(65,91):
            result = decrypt - 65
            result = 25 - result
            decrypt = result + 65
            atbash = chr(decrypt)
            
        elif decrypt in range(97,123):
            result = decrypt - 97
            result = 25 - result
            decrypt = result + 97
            atbash = chr(decrypt)
        
        elif decrypt<65 or decrypt>90 or decrypt <97 or decrypt>122:
            atbash = chr(decrypt)
        formal += atbash
        
    print("The result to decrypt is:" +formal)

elif select != "1" or select != "2":
    print("Choose from the above option")
