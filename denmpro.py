from pickle import TRUE
from re import A
import os




file = open("C:/Users/Asus/Documents/loggerr.txt","a",encoding="utf-8")




def function_1():
    print("function_1")
    user = input("Enter your name: ")
    password = input("Enter your password: ")
    if user == "admin" and password == "1234":
        print("Welcome")
        s4 =input("""
        <1> Toplama işlemi
        <2> Yazma işlemi
        
        """)
        if s4 == "1":
            while True:
                file = open("C:/Users/Asus/Documents/loggerr.txt","a",encoding="utf-8")
                asd = input("devam etmek isterseniz y yazınız:  eğer çıkmak isterseniz q yazınız: ")
                if(asd=="y"):
                   print("iki farklı sayıyı toplama işlemi")
                   sayi1 = int(input("sayı1: "))
                   sayi2 = int(input("sayı2: "))
                   print(sayi1+sayi2)
                   file.write(f"sayı1: {sayi1} ve sayı2: {sayi2} toplamı: {sayi1+sayi2}\n")
                   file.write("-----------------------------------------------------------\n")
                   continue
                elif(asd=="q"):
                   
                   print("programdan çıkılıyor")
                   break
        elif(s4=="2"):
            while True:
                     file = open("C:/Users/Asus/Documents/loggerr.txt","a",encoding="utf-8")
                     yazi = input("yazmak istediğiniz metni giriniz: ")
                     file.write(f"{yazi}\n")
                     file.write("-----------------------------------------------------------\n")
                     print("yazınız başarıyla yazıldı")
                     file.close()
                     continue
    else:
        print("hataı şifre")


function_1()
