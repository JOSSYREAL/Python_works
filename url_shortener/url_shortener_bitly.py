from bitly_api import *
from bitly_api import Connection
from tkinter import *
import pyshorteners
from PIL import ImageTk, Image
import pyperclip
import urllib
import time

#declaring the class variable
class UrlShortener:
    root = Tk()
    root.geometry('800x500+400+400')
    root.title('JR-Url_shortener')

    #this to load in the photo
    photo = PhotoImage(file = "uuu.png")
    # setting the image as icon
    root.iconphoto(False, photo)
    #to make the size of the screen not expandable above the specified screen resolution
    root.resizable(width= 'false', height='false')
    img = ImageTk.PhotoImage(Image.open("img.jpg"))
    background_img = Label(root, image=img)
    background_img.pack(fill=BOTH)
    #creating a string variable for storing what is entered in the entry box
    entered_url = StringVar()
    shortened_url = StringVar()
    def __init__(self):
        pass
    def url_shorten(self):
        #checking if the user entered the url
        #getting the entered url from the entered text variable of myentry
        self.urladdress = self.entered_url.get()
        #putting the token generated from bitly
        self.token1 = "6070e50a9fa9f917ffcf54311c8813227a562dc2"
        #we create the connection and access the bitly using the token
        try:
            self.api1 = Connection(access_token = self.token1)
            #now shorting the url using bitly
            self.response = self.api1.shorten(self.urladdress)
            # setting the received response to display on our label
            self.shortened_url.set(self.response['url'])
        except urllib.HTTPError:
            time.sleep(10)
            self.shortened_url.set("Poor or No intenet connection")
    def quit1(self):
        self.root.destroy()

    def copy2clipboard(self):
        #getting the shortened url from the shortned text variable
        self.url_short1 = self.shortened_url.get()
        #copying it to os clipboard using pyperclip
        pyperclip.copy(self.url_short1)


    def screen_view(self):
        self.text1 = Label(self.root, text="Enter url:", font= ("Ubuntu Light", 15), height= 2, width= 20, bg= "#004611", fg="white")
        self.text1.place(x=70, y=60)
        self.text2 = Label(self.root, text="Shortened url:", font= ("Ubuntu Light", 14), height= 2, width= 20, bg="#004611", fg="white")
        self.text2.place(x=70, y=180)
        #justify means where to start typing on screen--left or right
        self.myEntry = Entry(self.root, width=40,highlightbackground="#001122",font=("Verdana", 10),textvariable=self.entered_url, borderwidth = 10, justify=LEFT,highlightthickness=5, relief="flat",background="#127966")
        self.myEntry.place(x=370, y=60)
        self.view = Label(self.root, font= ("verdanda", 14), height= 2,textvariable=self.shortened_url, width= 31, bg="white", fg="#004611")
        self.view.place(x=370, y=180)
        self.but1 = Button(self.root,text= "Generate Short URL",  font=("verdanda", 14), height = 1, width= 15,relief='flat',borderwidth = 8, bg= "#000011", fg="gold",activebackground="#FF7956",command= lambda:self.url_shorten())
        self.but1.place(x=100, y=320)
        self.but2 = Button(self.root,text= "Copy to Clipboard",  font=("verdanda", 14), height = 1, width= 15,relief='flat',borderwidth = 8, bg= "#000011", fg="gold",activebackground="#FF7956",command= lambda:self.copy2clipboard())
        self.but2.place(x=325, y=320)
        self.but3 = Button(self.root,text= "Exit",  font=("verdanda", 14), height = 1, width= 10,relief='flat',borderwidth = 8, bg= "#000011", fg="gold",activebackground="#FF7956",command= lambda:self.quit1())
        self.but3.place(x=560, y=320)


obj_url_short = UrlShortener()
obj_url_short.screen_view()
