import random
lowerletters = "abcdefghijklmnopqrstuvwxyz"
upperletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]()-_*&$#@!"

def generate_password():
    length=int(input("Enter the password length:"))
    all=lowerletters+upperletters+numbers+symbols
    password="".join(random.sample(all,length))
    print("The password you generated is=",password)
generate_password()
