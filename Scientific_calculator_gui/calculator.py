from tkinter import *
from tkinter.font import Font
from math import *
import tkinter.messagebox
root=Tk()
root.title("JR-CALCULATOR")

#to resize the screen
root.geometry('470x405')
#to set the icon to your image
#this to load in the photo
photo = PhotoImage(file = "logo.png")
# setting the image as icon
root.iconphoto(False, photo)
#to make the size of the screen not expandable above the specified screen resolution
root.resizable(width= 'false', height='false')

#adding menu to the calculator 
#creating a menubar
# we are calling the constructor of the imported Menu module class and pass in
# our main GUI instance
menubar = Menu(root)
# we configure our GUI to use the just created Menu as the
# menu for our GUI
root.config(menu=menubar)
#defining text font
helv15 = Font(family="Bradley Hand ITC",size=15,weight="bold")

class Calculator:
    value2= 0.0
    operator1 = ""
    erase = False
    def __init__(self):
        self.internal_calc = False
    def __str__(self):
        return f'Scientific calculator'
    #configuring the menubar
    def to_exit(self):
        #returns true and false
        self.to_exit = tkinter.messagebox.askyesno("Close JR-Calculator?", "Confirm to quit")
        if self.to_exit:
            root.destroy()
    
    #button click to clear screen
    def button_click(self,number):
        
        if self.erase == True:
            myEntry.delete(0, "end")
            
            self.internal_calc = False
            self.erase = False
            
            
            

        if number == "pi":
            myEntry.delete(0, "end")
            myEntry.insert(0, pi)
        #if the value on the screen == 0, and the inputted number isnt .
        elif myEntry.get() == "0" and number != ".":
            myEntry.delete(0, "end")
            #to  get the index position of the number on the screen
            self.get_in = len(myEntry.get())
            #to diplay the inputted number at the specified position
            self.insert1= myEntry.insert(self.get_in, number)
        else:
            #to  get the index position of the number on the screen
            self.get_in = len(myEntry.get())
            #to display the enterd number at the index position
            self.insert1= myEntry.insert(self.get_in, number)

    def  clear_screen(self):
        myEntry.delete(0, "end")
        myEntry.insert(0, "0")
        self.value2= 0.0
        self.value1=0.0
        self.value3=0.0
        self.operator1 = ""
        self.internal_calc = False
        self.erase = False
        
        

    #for delete numbers one after the other
    def delete(self):
        #to  get the index position of the number on the screen
        self.get_in = len(myEntry.get())
        self.deleted = myEntry.delete(self.get_in-1)

   
    def placeholder(self, cal):
        
        if self.internal_calc == False:
            self.operator1 = cal
            self.value1 = float(myEntry.get())
            myEntry.delete(0, "end")
            self.value2 = self.value1
            self.internal_calc = True
            return
        else:
            self.operator2 = cal
            self.equal_to()
            self.operator1 = cal
            return
        
        

            
    #creating a placeholder function
    def equal_to(self, ans= None):
        self.ans= ans
        if self.ans == "ans":
            erase=True
            self.internal_calc= False
        # global value1, operator, myEntry
        if self.operator1 == "+":
            if self.internal_calc == False:
                self.value3 = float(myEntry.get())
                self.result = self.value2 + self.value3
                self.value2 = self.result
                myEntry.delete(0, "end")
                myEntry.insert("end", self.result)
            elif self.internal_calc== True:
                self.value3 = float(myEntry.get())
                myEntry.delete(0, "end")
                self.result = self.value2 + self.value3
                self.value2 = self.result
                return
            
        elif  self.operator1 == "-":
            if self.internal_calc == False:
                self.value3 = float(myEntry.get())
                self.result = self.value2 - self.value3
                self.value2 = self.result
                myEntry.delete(0, "end")
                myEntry.insert("end", self.result)
            elif self.internal_calc == True:
                self.value3 = float(myEntry.get())
                myEntry.delete(0, "end")
                self.result = self.value2 - self.value3
                self.value2 = self.result
                return
        elif  self.operator1 == "*":
            if self.internal_calc == False:
                self.value3 = float(myEntry.get())
                self.result = self.value2 * self.value3
                self.value2 = self.result
                myEntry.delete(0, "end")
                myEntry.insert("end", self.result)
            elif self.internal_calc== True:
                self.value3 = float(myEntry.get())
                myEntry.delete(0, "end")
                self.result = self.value2 * self.value3
                self.value2 = self.result
                return
            
        elif  self.operator1 == "/":
            if self.internal_calc == False:
                self.value3 = float(myEntry.get())
                self.result = self.value2 / self.value3
                self.value2 = self.result
                myEntry.delete(0, "end")
                myEntry.insert("end", self.result)
            elif self.internal_calc== True:
                self.value3 = float(myEntry.get())
                myEntry.delete(0, "end")
                self.result = self.value2 / self.value3
                self.value2 = self.result
                return
            
        elif self.operator1 == "exp":
            if self.internal_calc == False:
                self.value3 = float(myEntry.get())
                self.result = self.value2*(10**int(self.value3))
                self.value2 = self.result
                myEntry.delete(0, "end")
                myEntry.insert("end", self.result)
            elif self.internal_calc== True:
                self.value3 = float(myEntry.get())
                myEntry.delete(0, "end")
                self.result = self.value2*(10**int(self.value3))
                self.value2 = self.result
                return
            
        elif self.operator1 == "pow":
            if self.internal_calc == False:
                self.value3 = float(myEntry.get())
                self.result = self.value2**int(self.value3)
                self.value2 = self.result
                myEntry.delete(0, "end")
                myEntry.insert("end", self.result)
            elif self.internal_calc== True:
                self.value3 = float(myEntry.get())
                myEntry.delete(0, "end")
                self.result = self.value2**int(self.value3)
                self.value2 = self.result
                return
            
        elif self.operator1 == "mod":
            if self.internal_calc == False:
                self.value3 = float(myEntry.get())
                self.result = self.value2%self.value3
                self.value2 = self.result
                myEntry.delete(0, "end")
                myEntry.insert("end", self.result)
            elif self.internal_calc == True:
                self.value3 = float(myEntry.get())
                myEntry.delete(0, "end")
                self.result = self.value2%self.value3
                self.value2 = self.result
                return
            
        
        
        self.internal_calc = False
        self.erase = True
        

    
        
    #creating the direct value function --for one value button
    def one_click(self, cal):
        # global value1, operator, myEntry
        self.value=myEntry.get()
        self.value1 =float(myEntry.get())
        self.operator = cal
        if self.operator == "sqrt":
            self.result= sqrt(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "±":
            self.result= (-1*self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "." and "." not in self.value:
            self.result = self.value+"."
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "sin":
            self.result= sin(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "cos":
            self.result= cos(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "tan":
            self.result= tan(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "sinh":
            self.result= sinh(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "cosh":
            self.result= cosh(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "tanh":
            self.result= tanh(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "sin":
            self.result= sin(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "log":
            self.result= log(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "ln":
            self.result= log10(self.value1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "pow-1":
            self.result= pow(self.value1,-1)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "pow2":
            self.result= pow(self.value1,2)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        elif self.operator == "pow3":
            self.result= pow(self.value1,3)
            myEntry.delete(0, "end")
            myEntry.insert(0, self.result)
        
    def scientific(self):
        root.geometry('820x385')
        #to make the size of the screen not expandable above the specified screen resolution
        root.resizable(width= 'false', height='false')  
        header = Label(root, text=calcu_obj, font= ("verdanda", 15), height= 2, width= 8, bg= "#000011", fg="white")
        header.grid(row=0,column=4,columnspan=3, padx=0, ipady=2,pady=0, sticky=EW)
        #defining the scientific button
        but20 = Button(root,text= "Sin",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("sin"))
        but20.grid(row=1, column=4, sticky=EW)
        #pi
        but21 = Button(root,text= "Cos",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("cos"))
        but21.grid(row=1, column=5, sticky=EW)
        but22 = Button(root,text= "Tan",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("tan"))
        but22.grid(row=1, column=6, sticky=EW)
        but23 = Button(root,text= "Log",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("log"))
        but23.grid(row=2, column=4, sticky=EW)
        but24 = Button(root,text= "x^y",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda:calcu_obj.placeholder("pow"))
        but24.grid(row=2, column=5, sticky=EW)
        but25 = Button(root,text= "Ln",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("ln"))
        but25.grid(row=2, column=6, sticky=EW)
        but26 = Button(root,text= "π",  font=("verdan da", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda:calcu_obj.button_click("pi"))
        but26.grid(row=3, column=4, sticky=EW)
        but27 = Button(root,text= "x^-1",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("pow-1"))
        but27.grid(row=3, column=5, sticky=EW)
        but28 = Button(root,text= "Exp",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.placeholder("exp"))
        but28.grid(row=3, column=6, sticky=EW)
        but29 = Button(root,text= "x^2",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("pow2"))
        but29.grid(row=4, column=4, sticky=EW)
        but30 = Button(root,text= "x^3",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("pow3"))
        but30.grid(row=4, column=5, sticky=EW)
        but31 = Button(root,text= "Mod",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.placeholder("mod"))
        but31.grid(row=4, column=6, sticky=EW)
        but25 = Button(root,text= "Sinh",  font=("verdanda", 16), height = 2, width= 9,relief='flat',bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("sinh"))
        but25.grid(row=5, column=4, sticky=EW)
        but25 = Button(root,text= "Cosh",  font=("verdanda", 16), height = 2, width= 9,relief='flat',bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("cosh"))
        but25.grid(row=5, column=5, sticky=EW)
        but25 = Button(root,text= "Tanh",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda:calcu_obj.one_click("tanh"))
        but25.grid(row=5, column=6, sticky=EW)
    def standard(self):
        root.geometry('470x385')
        #to make the size of the screen not expandable above the specified screen resolution
        root.resizable(width= 'false', height='false')
    def cut(self):
        # global copied_value
        self.copied_value=myEntry.get()
        myEntry.delete(0, "end")
    def copy(self):
        # global copied_value
        self.copied_value=myEntry.get()
    def paste(self):
        myEntry.insert(0, self.copied_value)
    def help(self):
        #returns true and false
        self.to_exit_help = tkinter.messagebox.showinfo("info","This is a standard and a scientific calculator developed by Jossyreal@Fastrack Nigeria")#askyesno("Close JR-Calculator?", "Confirm to quit")






#creating the calculator obj instance
calcu_obj = Calculator()

# creating menu and adding menubar
#turning the tearoff cmd off to remove the dashed line that by default appears at the file menu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Standard", command=lambda: calcu_obj.standard())
file_menu.add_command(label="Scientific", command=lambda: calcu_obj.scientific())
file_menu.add_separator()
file_menu.add_command(label= "Exit", command=lambda: calcu_obj.to_exit())
#adding file_menu to the menu bar and giving it a label
menubar.add_cascade(label="File", menu=file_menu)

edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: calcu_obj.cut())
edit_menu.add_command(label="Copy", command=lambda: calcu_obj.copy())
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=lambda: calcu_obj.paste())
menubar.add_cascade(label="Edit", menu= edit_menu)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="View Help", command=lambda: calcu_obj.help())
menubar.add_cascade(label="Help", menu= help_menu)




#variable for label/text
header = Label(root, text="Display", font= helv15, height= 2, width= 8, bg= "#000011", fg="white")
header.grid(row=0,column=0, padx=0, pady=0, sticky=EW)

#defining the input/entry position
myEntry = Entry(root, width=10,highlightbackground="#000011",font=("Verdana", 20), borderwidth = 0, justify=RIGHT,highlightthickness=5, relief="ridge",background="#66CC99")
#setting its position
myEntry.grid(row=0,column=1, columnspan=3,padx=0,pady=0, ipady=6,sticky=EW)


#button
#Defining the buttons
#the reason why we use lambda is that you cant just put parenthesis direct
#the relief means to set the button display to flat/straight
#activebackground means the background when the button is pressed
but1 = Button(root,text= "1", font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(1))
#putting the buttons on the screen
but1.grid(row=1, column=0, sticky=EW)
but2 = Button(root,text= "4",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(4))
but2.grid(row=2, column=0, sticky=EW)
but3 = Button(root,text= "7",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(7))
but3.grid(row=3, column=0, sticky=EW)
but4 = Button(root,text= ".",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue", command= lambda: calcu_obj.one_click("."))
but4.grid(row=4, column=0, sticky=EW)

but4 = Button(root,text= "2",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(2))
but4.grid(row=1, column=1, sticky=EW)
but5 = Button(root,text= "5",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(5))
but5.grid(row=2, column=1, sticky=EW)
but6 = Button(root,text= "8",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(8))
but6.grid(row=3, column=1, sticky=EW)
but7 = Button(root,text= "0",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(0))
but7.grid(row=4, column=1, sticky=EW)
but8 = Button(root,text= "3",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(3))
but8.grid(row=1, column=2, sticky=EW)
but9 = Button(root,text= "3",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(3))
but9.grid(row=1, column=2, sticky=EW)
but10 = Button(root,text= "6",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue", command= lambda: calcu_obj.button_click(6))
but10.grid(row=2, column=2, sticky=EW)
but11 = Button(root,text= "9",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000066", fg="white",activebackground="blue",command= lambda: calcu_obj.button_click(9))
but11.grid(row=3, column=2, sticky=EW)
but12 = Button(root,text= "÷",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.placeholder("/"))
but12.grid(row=4, column=2, sticky=EW)
but13 = Button(root,text= "-",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.placeholder("-"))
but13.grid(row=1, column=3, sticky=EW)
but14 = Button(root,text= "+",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.placeholder("+"))
but14.grid(row=2, column=3, sticky=EW)
but15 = Button(root,text= "*",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.placeholder("*"))
but15.grid(row=3, column=3, sticky=EW)
but16 = Button(root,text= "=",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.equal_to("ans"))
but16.grid(row=5, column=3, sticky=EW)
#delete
but17 = Button(root,text= "Delete",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.delete())
but17.grid(row=5, column=0, sticky=EW)
#clear
but18 = Button(root,text= "Clear",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.clear_screen())
but18.grid(row=5, column=1, sticky=EW)
#mod
but19 = Button(root,text= "±",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.one_click("±"))
but19.grid(row=5, column=2, sticky=EW)

#sqrt
but22 = Button(root,text= "√",  font=("verdanda", 16), height = 2, width= 9,relief='flat', bg= "#000011", fg="white",activebackground="blue",command= lambda: calcu_obj.one_click("sqrt"))
but22.grid(row=4, column=3, sticky=EW)
# #exp

#calling out the figure
root.mainloop()
