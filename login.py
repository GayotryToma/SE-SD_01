from tkinter import *

root=Tk()
root.title("Login")
root.geometry("600x470")
root.resizable(False,False)

def login():
    print("login")

Label(root,text="Login your account",font="arial 25").pack(pady=50)


Label(text="Email",font=23).place(x=100,y=200)
Label(text="Password",font=23).place(x=100,y=250)


#entry

emailValue=StringVar()
passValue=StringVar()



emailEntry=Entry(root,textvariable=emailValue,width=30,bd=2,font=20)
passEntry=Entry(root,textvariable=passValue,width=30,bd=2,font=20)


emailEntry.place(x=200,y=200)
passEntry.place(x=200,y=250)
#check button
checkValue=IntVar
checkbtn=Checkbutton(text="remember me?",variable=checkValue)
checkbtn.place(x=200,y=300)

Button(text="login",font=20,width=11,height=2,command=login).place(x=250,y=380)

root.mainloop()