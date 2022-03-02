from ast import While
import os
from tkinter import W

from numpy import true_divide



while True:
    dosya = input('''okunmasını istediğiniz dosyanın yolunu giriniz: 
örnek = C:/Users/Asus/Documents/dosya_adi.txt
     : ''')
    os.system("cls")

    filee = open(f"{dosya}","r",encoding="utf-8")

    okunan = filee.read()


    print(okunan)
    filee.close()

    text = input("Dosya içeriğini silmek istermisiniz y/n: ")
    if(text=="y"):
       filee.close()
       filee = open("C:/Users/Asus/Documents/loggerr.txt","w",encoding="utf-8")
       filee.write("")
       filee.close()
       print("dosya içeriği silindi")
       continue
    else:
       print("dosya içeriği silinmedi")
       os.system("cls")
       filee.close()
       continue



