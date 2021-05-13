print("Pratyush Avi A203")
print("Enter 3 key")
key = []
for n in range(0,3):
    ele = int(input("Enter key:"))
    key.append(ele)
print("The key are:",key)
choice = input("Do you want to perform Encryption(E) or Decryption(D)?")
word = input("Enter word to be converted:")
    
lis = []
for i in word:
    if ord(i) in range(65,91):
        lis.append(ord(i))
    elif ord(i) in range(97,123):
        lis.append(ord(i))
    elif ord(i)<65 or ord(i)>90 or ord(i)<97 or ord(i)>122:
        lis.append(ord(i))
newlist = lis
print("ASCII values of each character in plan text:",newlist,"\n")

trans = []

if choice.upper() == "E":
    for char in newlist:
        if char in range(65,91):
            if newlist.index(char)%3 == 0:
                ele = ((((char-65)+key[0])%26)+65)
                if ele > 90:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-65)+key[1])%26)+65)
                if ele > 90:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-65)+key[2])%26)+65)
                if ele > 90:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
        elif char in range(97,123):
            if newlist.index(char)%3 == 0:
                ele = ((((char-97)+key[0])%26)+97)
                if ele > 122:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-97)+key[1])%26)+97)
                if ele > 122:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-97)+key[2])%26)+97)
                if ele > 122:
                    ele = ele - 26
                    trans.append(ele)
                else:
                    trans.append(ele)              
        elif char<65 or char>90 or char<97 or char>122:
            trans.append(char)

elif choice.upper() == "D":
    for char in newlist:
        if char in range(65,91):
            if newlist.index(char)%3 == 0:
                ele = ((((char-65)-key[0])%26)+65)
                if ele > 90:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-65)-key[1])%26)+65)
                if ele > 90:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-65)-key[2])%26)+65)
                if ele > 90:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
        elif char in range(97,123):
            if newlist.index(char)%3 == 0:
                ele = ((((char-97)-key[0])%26)+97)
                if ele > 122:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 1:
                ele = ((((char-97)-key[1])%26)+97)
                if ele > 122:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)
            elif newlist.index(char)%3 == 2:
                ele = ((((char-97)-key[2])%26)+97)
                if ele > 122:
                    ele = ele + 26
                    trans.append(ele)
                else:
                    trans.append(ele)              
        elif char<65 or char>90 or char<97 or char>122:
            trans.append(char)

elif choice != "E" or choice != "D" or choice != "e" or choice != "d":
    print("Enter Option As E,e,D or d!!!")

print("ASCII values of each character in Cipher text:",trans,"\n")
result=[]
for value in trans:
    if value == " ":
        result.append(" ")
    else:
        result.append("".join(chr(value)))

final=""
for ch in result:
    final += ch
print("The Converted Cipher Text:",final)

