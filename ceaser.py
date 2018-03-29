# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 08:00:16 2018

@author: Binish125
"""

import random

class ceaser:
    key=0

    def __init__(self):
        self.key=random.randint(0,26)
        
    def encrypt(self,plain_text):
        print("\nEncryption Key:\t"+str(self.key))
        cipher_list=[]
        plain_list=list(plain_text)
        for chara in plain_list:
            if(ord(chara)!=32):
                char_code=ord(chara)%97
                cipher_value=((char_code+self.key)%26)+97
                cipher_char=chr(cipher_value)
            else:
                cipher_char=" "
            cipher_list.append(cipher_char)
        cipher_text=''.join(cipher_list)
        return(cipher_text)
        
    def decrypt(self,cipher_text):
        plain_list=[]
        cipher_list=list(cipher_text)
        for chara in cipher_list:
            if(ord(chara)!=32):
                char_code=ord(chara)%97
                plain_value=((char_code-self.key)%26)+97
                plain_char=chr(plain_value)
            else:
                plain_char=" "
            plain_list.append(plain_char)
        plain_text="".join(plain_list)
        return(plain_text) 
       

plain_text=input("\nEnter your text : ")
x=ceaser()
cipher=x.encrypt(plain_text)
print("\n\nCipher text : \t"+cipher)
plain=x.decrypt(cipher)
print("\n\nPlain_text : \t"+plain)