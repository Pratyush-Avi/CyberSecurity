print("PRATYUSH AVI")
select = input("Enter 1. Encryption or 2. Deceyption ?")

if select == "1":
    plaintext = input("Enter Plain Text:")
    key = input("Enter key:")
    if(len(key) == len(plaintext)):

        def split(pt):
            return list(pt)
        
        ptlist = []
        for j in plaintext:
            ptlist.append(ord(j)-65)
    
        klist = []
        for k in key:
            klist.append(ord(k)-65)
    
        sum = []
        for i in range(0,len(ptlist)):
            add = ptlist[i]+klist[i]+65
            if add>90:
                add = add-26
                sum.append(add)
            else:
                sum.append(add)
                
        result=[]
        for value in sum:
            result.append("".join(chr(value)))
        
        final=""
        for ch in result:
            final += ch
        print("Cipher Text:",final)
        
    else:
        print("Error: Length of key is not equal to length of plaintext!!!")

elif select == "2":
    plaintext = input("Enter Cipher Text:")
    key = input("Enter key:")
    if(len(key) == len(plaintext)):
        encrypt = ""
    
        def split(pt):
            return list(pt)
        
        ptlist = []
        for j in plaintext:
            ptlist.append(ord(j)-65)
        
        klist = []
        for k in key:
            klist.append(ord(k)-65)
        
        sum = []
        for i in range(0,len(ptlist)):
            add = ptlist[i]-klist[i]+65
            if add<65:
                add = add+26
                sum.append(add)
            else:
                sum.append(add)
            
        result=[]
        for value in sum:
            result.append("".join(chr(value)))
        
        final=""
        for ch in result:
            final += ch
        print("Decryption:",final)
        
    else:
        print("ERROR: Length of key is not equal to length of plaintext!!!")
    
elif select !="1" or select !="2":
    print("Choose from the above option")
