

from tkinter import *
import string
from random import sample
# using pandas to copy to clipboard
from pandas.io import clipboard
from PIL import ImageTk, Image
import os
from tkinter.font import Font

# # defining the app layout root
# root = Tk()

#defining the app screen resolution
class PasswordGen:
    root = Tk()
    poor = string.ascii_uppercase + string.ascii_lowercase
    average = poor + string.digits
    advanced = average + string.punctuation
    #intvar is used to get more than one integer value at a time
    # StringVar is used to get more than one string value at a time
    #to get more integer and string variable


    helv15 = Font(family="verdanda",size=30,weight="bold")
    #defining the constructor
    def __init__(self):
        self.name = ""
        self.password= ""



    def home_view(self):

        self.root.geometry("700x400")
        self.root.title("JR-Password_Generator")
        #to set the icon to your imageb
        #this to load in the photo
        self.photo = PhotoImage(file = "uuu.png")
        # setting the image as icon
        self.root.iconphoto(False, self.photo)
        #to make the size of the screen not expandable above the specified screen resolution
        self.root.resizable(width= 'false', height='false')
        # root.config(background="#CC0033", color="orange")
        self.img = ImageTk.PhotoImage(Image.open("data(2).jpg"))
        # self.background_img = Label(root, image=self.img)
        c = Canvas()
        c.create_image(0, 0, image=self.img)
        c.place(x=-10, y=-10, relwidth=11, relheight=11)
        # c.pack()

        # and now the text at coordinates (50, 50)

        # self.background_img.place(x=0, y=0, relwidth=1, relheight=1)
        c.create_text(360,  100, text="Secured Password Generator",font=self.helv15, fill="white")
        # c.create_text(350, 150, text="JR Secured Password Generator",font=("adobe caslon pro bold", 30), fill="#FFCCCC")
    def quit1(self):
        self.root.destroy()
    def quit2(self):
        self.root2.destroy()

    def display2(self):
        self.length_label = StringVar()
        self.title= StringVar()
        self.name1= self.myEntry1.get()
        self.name+=self.name1
        self.root.destroy()
        self.root2=Tk()
        self.root2.geometry("700x400")
        self.root2.title("JR-Password_Generator")
        #to set the icon to your image
        #this to load in the photo
        self.photo = PhotoImage(file ="uuu.png")
        # setting the image as icon
        self.root2.iconphoto(False, self.photo)
        #to make the size of the screen not expandable above the specified screen resolution
        self.root2.resizable(width= 'false', height='false')
        self.root2.config(background="#CC0033")
        self.text3 = Label(self.root2, text="User name:", font= ("verdanda", 15), height= 2, width= 20, bg= "#000011", fg="white")
        self.text3.place(x=70, y=40)
        self.text4 = Label(self.root2, text="Password Generated:", font= ("verdanda", 14), height= 2, width= 20, bg="#000011", fg="white")
        self.text4.place(x=70, y=100)
        self.choice= IntVar()
        self.text_var = IntVar()
        self.myEntry2 = Entry(self.root2, width=30,highlightbackground="#001122",font=("Verdana", 10), borderwidth = 10, justify=RIGHT,highlightthickness=5, relief="flat",background="#FF7956")
        # myEntry = Entry(root,width=10).pack()
        self.myEntry2.place(x=360, y=100)
        self.myEntry3 = Entry(self.root2, width=30,highlightbackground="#001122",font=("Verdana", 10), borderwidth = 10, justify=CENTER,highlightthickness=5, relief="flat",background="#FF7956")
        # myEntry = Entry(root,width=10).pack()
        self.myEntry3.place(x=360, y=40)
        self.myEntry3.delete(0, "end")
        self.myEntry3.insert(0, self.name)
        # self.label2 = Label(self.root2, textvariable=self.title, bg="red", fg="black", width=20).place(x=70, y=200)
        # self.title.set("the strength of the password:")
        self.label2 = Label(self.root2, text="Password length (8-24):", font= ("verdanda", 15), height= 2, width= 20, bg= "#000011", fg="white").place(x=70, y=160)
        #creating radio button
        self.rad1 = Radiobutton(self.root2, text="uppercase and lowercase", variable=self.choice, value=1,background="#FF7956",width=30, command= lambda: self.selection()).place(x=360, y=220)
        self.rad2 = Radiobutton(self.root2, text="uppercase, lowercase, digit", variable=self.choice, value=2,background="#FF7956",width=30, command= lambda: self.selection()).place(x=360, y=260)
        self.rad3 = Radiobutton(self.root2, text="uppercase, lowercase, digit, symbol", variable=self.choice, value=3,background="#FF7956",width=30, command= lambda: self.selection()).place(x=360, y=300)
        # self.length_label3 = Label(self.root2, textvariable = self.length_label,width=20, bg="green", fg="black").place(x=70, y=160)
        self.length_label3 = Label(self.root2, text="Password strength:",font= ("verdanda", 15), height= 2, width= 20, bg= "#000011", fg="white").place(x=70, y=220)
        # self.length_label.set("password length: (8-24)")
        #creating spinbox
        self.spin_box = Spinbox(self.root2, from_ = 8, to_ = 24, textvariable=self.text_var, highlightbackground="#001122",font=("Verdana", 11), borderwidth = 10, justify=CENTER,highlightthickness=5, relief="flat",background="#FF7956", width=22).place(x=360, y=160)
        self.but1 = Button(self.root2, text= "Generate Password",background="#000011", width= 27,fg="#FF7956",activebackground="#FF7956",highlightbackground="#001122",command=lambda: self.pass_gen()).place(x=70, y=280)
        self.but2 = Button(self.root2, text= "Exit", background="#000011", width= 20,fg="#FF7956",activebackground="#FF7956",highlightbackground="#001122",command=lambda: self.quit2()).place(x=470, y=340)
        self.but2 = Button(self.root2, text= "Home Screen", background="#000011", width= 20,fg="#FF7956",activebackground="#FF7956",highlightbackground="#001122",command=lambda: self.back_to_homescreen()).place(x=270, y=340)
        self.but3 = Button(self.root2, text= "Copy to clipboard", background="#000011", width= 20,fg="#FF7956",activebackground="#FF7956",highlightbackground="#001122",command=lambda: self.clipboard_copy()).place(x=70, y=340)
        self.root2.mainloop()

    def back_to_homescreen(self):
        self.root2.destroy()
        self.name = ""
        self.root = Tk()
        self.poor = string.ascii_uppercase + string.ascii_lowercase
        self.average = self.poor + string.digits
        self.advanced = self.average + string.punctuation
        #intvar is used to get more than one integer value at a time
        # StringVar is used to get more than one string value at a time
        #to get more integer and string variable
        self.helv15 = Font(family="verdanda",size=30,weight="bold")
        self.home_view()
        self.text_display()
        self.root.mainloop()

    def text_display(self):
        self.text1 = Label(self.root, text="Enter your name to start", font= ("verdanda", 15), height= 2, width= 25, bg= "#000011", fg="white")
        self.text1.place(x=45, y=180)
        self.text2 = Label(self.root, text="Press Enter to Start or Exit to Quit", font= ("verdanda", 14), height= 2, width= 29, bg="#000011", fg="white")
        self.text2.place(x=45, y=240)
        # text3 = Label(root, text="Enter your name to start", font= ("verdanda", 15), height= 2, width= 25, bg= "#000011", fg="white")
        # text3.place(x=80, y=180)
        # text4 = Label(root, text="Press exit to quit", font= ("verdanda", 15), height= 2, width= 25, bg= "#000011", fg="white")
        # text4.place(x=80, y=240)
        self.myEntry1 = Entry(self.root, width=30,highlightbackground="#000011",font=("Verdana", 10), borderwidth = 11, justify=LEFT,highlightthickness=5, relief="flat",background="#FF7956")
        # myEntry = Entry(root,width=10).pack()
        self.myEntry1.place(x=380, y=180)
        self.but1 = Button(self.root,text= "Exit",  font=("verdanda", 14), height = 1, width= 10,relief='flat',borderwidth = 8, bg= "#000011", fg="#FF7956",activebackground="#FF7956",command= lambda:self.quit1())
        self.but1.place(x=380, y=240)
        self.but2 = Button(self.root,text= "Enter",  font=("verdanda", 14), height = 1, width= 10,relief='flat',borderwidth = 8, bg= "#000011", fg="#FF7956",activebackground="#FF7956",command= lambda:self.display2())
        self.but2.place(x=520, y=240)


    #defining the  radio button selection
    def selection(self):
        self.choice.get()

    def clipboard_copy(self):
        clipboard.copy(self.myEntry2.get())
        # self.label1 = Label(root, textvariable=title, bg="red").pack()
        # self.title.set("Choose the type of strength for the password:")

    def pass_gen(self):
        if self.choice.get() == 1:
            self.password1= self.password.join(sample(self.poor, self.text_var.get()))
            self.myEntry2.delete(0, "end")
            self.myEntry2.insert(0, self.password1)

        elif self.choice.get() == 2:
            self.password1= self.password.join(sample(self.average, self.text_var.get()))
            self.myEntry2.delete(0, "end")
            self.myEntry2.insert(0, self.password1)
        elif self.choice.get() == 3:
            self.password1= self.password.join(sample(self.advanced, self.text_var.get()))
            self.myEntry2.delete(0, "end")
            self.myEntry2.insert(0, self.password1)
obj_password = PasswordGen()
obj_password.home_view()
obj_password.text_display()
obj_password.root.mainloop()

