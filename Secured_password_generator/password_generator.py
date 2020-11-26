import string
import random
from random import sample,shuffle

class PasswordGen:

    letter_lst = []
    digit_lst= list()
    symbol_lst = []
    password_lst=[]
    def __init__(self, name):
        self.password = ""
        self.name = name

    def __str__(self):
        return f'Name: {self.name}\nPassword: {self.password}'

    def passkey(self):
        for letter in string.ascii_letters:
            self.letter_lst.append(letter)
        self.password_lst+=[item for item in (sample(PasswordGen.letter_lst,3))]
        for number in string.digits:
            self.digit_lst.append(number)
        self.password_lst+=[item for item in (sample(PasswordGen.digit_lst,3))]
        for symbol in string.punctuation:
            self.symbol_lst.append(symbol)
        self.password_lst+=[item for item in (sample(PasswordGen.symbol_lst,3))]
        #to scatter the items in the lst randomly
        shuffle(self.password_lst)
        self.password+="".join(str(i) for i in self.password_lst)
        return self.password

Name = input("Welcome to secured password generator\nEnter your name: ")
inst_pass = PasswordGen(Name)
print(f"Congratulation!!! {inst_pass.name}\nYour generated secured password is: {inst_pass.passkey()}\nPlease, keep it safe")





