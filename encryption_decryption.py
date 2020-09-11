code=input("enter your code:")
distance=input("enter the distance value:")
distance=int(distance)

# reversing the string

reversedcode=code[::-1]
print("reversed string is: " + reversedcode)

encyrptmsg=""

for ch in reversedcode:
    ordinalvalue=ord(ch)
    ciphervalue = ordinalvalue + distance
    if ciphervalue>ord("z"):
        x=ciphervalue-ord("z")
        ciphervalue=ord("a")+x-1

    encyrptmsg=encyrptmsg+chr(ciphervalue)

print("encyrypted message is: " + encyrptmsg)


code=input("enter your code:")
distance=input("enter the distance value:")
distance=int(distance)

reversedcode=code[::-1]
print("reversed string is: " + reversedcode)

decyrptmsg=""

for ch in reversedcode:
    ordinalvalue=ord(ch)
    ciphervalue=ordinalvalue-distance
    if ciphervalue < ord("a"):
        x=ord("a")-ciphervalue
        ciphervalue=ord("z")-x+1

    decyrptmsg=decyrptmsg+chr(ciphervalue)

print("decyryptedmsg is: " + decyrptmsg)