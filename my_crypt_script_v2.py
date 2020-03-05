print(""" This is my  Cipher Module:
Firest you need to select Encryption type,
Second select either Encryption OR Decryption,
Third you will be asked to enter your selected KEY,
then Finally the text to be Coded OR Decoded""")
selection=0
direction=0
text=""
def visenere():
    global cipher_txt
    global direction
    key=input ("input the Encryption key: ")
    key_len=len(key)
    key=key.upper()
    j=0
    plain_txt=input("input the text: ")
    plain=plain_txt.upper()
    cipher_txt=""
    for i in range (len(plain_txt)):
        if  ord(plain[i])>= 65 and ord(plain[i])<= 90:
            cipher_ascii= (direction*ord(key[j])+ord(plain[i])-130)%26+65
            cipher=chr(cipher_ascii)
            cipher_txt=cipher_txt+cipher
        else:
            j=j-1
            cipher_txt=cipher_txt+plain[i]
    
        if j == key_len-1:
            j=-1
        j=j+1
def Caesar():
    global cipher_txt
    global direction
    key=input ("input the Encryption key (Number): ")
    key= int(key)%26
    plain_txt=input("input the text: ")
    plain=plain_txt.upper()
    cipher_txt=""
    for i in range (len(plain_txt)):
        if  ord(plain[i])>= 65 and ord(plain[i])<= 90:
            cipher_ascii= (direction*key + ord(plain[i])-65)%26+65
            cipher=chr(cipher_ascii)
            cipher_txt=cipher_txt+cipher
        else:
            cipher_txt=cipher_txt+plain[i]

def select_cipher():
    global selection
    selection ="0"
    while selection =="0":
        selection= input ("""
        Please select:
        1- Visenere Cipher
        2- Caesar Cipher
        3- Exit
        Selection is :""")
        if selection =="1":
            selection = 1
        elif selection =="2":
            selection = 2
        elif selection =="3":
            selection = 3
        else:
            selection ="0"
            print("InCorrect Selection, Try again:")
def direction_fun():
    global direction
    direction ="0"
    if selection==3:
        pass
    else:
        while direction =="0":
            direction= input ("""
            Please select:
            1- Encrypt
            2- Decrypt
            3- Go Back
            4- Exit
            Mode is :""")
            if direction =="1":
                direction = 1
            elif direction =="2":
                direction = -1
            elif direction =="3":
                direction = 3
            elif direction =="4":
                direction = 4
            else:
                direction ="0"
                print("InCorrect Selection, Try again:")
def print_fun():
    global direction
    global selection
    if direction ==1:
        text="Cipher "
        print("The "+text+"message is: ",cipher_txt)
        selection=0
        direction=0
    elif direction ==-1:
        text="Plain "
        print("The "+text+"message is: ",cipher_txt)
        selection=0
        direction=0
    elif direction ==4:
     	print("Bye")
    

while selection ==0 and direction ==0:
    select_cipher()
    direction_fun()
    
    if direction ==4:
        pass
    elif selection ==3:
        pass
    elif direction ==3:
        direction=0
        selection=0
    elif selection==1:
        visenere()
    elif selection==2:
        Caesar()
    print_fun()
   

