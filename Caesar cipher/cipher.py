from math import *
from string import *
from array import *

alphabet = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',
            13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

specChar = {0:"~",1:".",2:"?",3:";",4:":",5:"!",6:"@",7:"$",8:"%",9:"^",10:"&",11:"(",
            12:")",13:"+",14:"-",15:"*",16:"/",17:"<",18:">",19:"`",20:"#",21:"\"",22:"'",23:","}

def isSpecialChar(element):
    for char in specChar:
        if(element == specChar[char]):
            return True
    return False

def isCharacter(element):
    for letter in alphabet:
        if(element.lower() == alphabet[letter]):
            return True
    return False       

def isNumber(element):
    for i in range(0,10):
        if(int(element) == i):
            return True
    return False

def encrypt(message, encryptNum):
    encryptedMessage = "";
   
    for mElement in message:
        if(mElement == " "):
            encryptedMessage = encryptedMessage + " "
        elif(mElement == "."):
            encryptedMessage = encryptedMessage + "."
        elif(isSpecialChar(mElement)):
            for aCharacter in specChar:
                if(mElement == specChar[aCharacter]):
                    eChar = (aCharacter + encryptNum)%24
                    encryptedMessage = encryptedMessage + specChar[eChar]
        elif(isCharacter(mElement)):
            for aLetter in alphabet:
                if(mElement.lower() == alphabet[aLetter]):
                    eLetter = (aLetter + encryptNum)%26
                    encryptedMessage = encryptedMessage + alphabet[eLetter]
        elif(isNumber(mElement)):
            eNumber = (int(mElement) + encryptNum)%10
            encryptedMessage = encryptedMessage + str(eNumber)
        else:
            encryptedMessage = encryptedMessage + mElement

    print("\n%s  \nDecryption Number: %d\n" %(encryptedMessage, encryptNum))
    return encryptedMessage

def decrypt(message, decryptNum):
    decryptedMessage = "";
   
    for mElement in message:
        if(mElement == " "):
            decryptedMessage = decryptedMessage + " "
        elif(mElement == "."):
            encryptedMessage = encryptedMessage + "."
        elif(isSpecialChar(mElement)):
            for aCharacter in specChar:
                if(mElement == specChar[aCharacter]):
                    deChar = (aCharacter - decryptNum)%24
                    decryptedMessage = decryptedMessage + specChar[deChar]
        elif(isCharacter(mElement)):
            for aLetter in alphabet:
                if(mElement.lower() == alphabet[aLetter]):
                    deLetter = ((aLetter - decryptNum)%26)
                    decryptedMessage = decryptedMessage + alphabet[deLetter]
        elif(isNumber(mElement)):
            deNumber = (int(mElement) - decryptNum)%10
            decryptedMessage = decryptedMessage + str(deNumber)
        else:
            decryptedMessage = decryptedMessage + mElement

    print("Decrtypted Message: %s\n" %(decryptedMessage))
    return decryptedMessage


if __name__ == '__main__':

    deORen = input("Would you like to encrypt a message or decrypt a message? (e or d): ")
    if(deORen == "e"):
        message = input("Please enter message to encrypt: ")
        encryptNum = int(input("Please enter the Caesar Cipher encryption number: "))
        encrypt(message, encryptNum)
    elif(deORen == "d"):
        message = input("Please enter message to decrypt: ")
        decryptNum = int(input("Please enter the Caesar Cipher encryption number: "))
        decrypt(message,decryptNum)
