from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root=Tk()
root.title("FileEDroP")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False,False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select Image File',
                                            filetype=(('file type','*.txt'),('all files','*.*')))
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections.... ')
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully")




    #icon
    image_icon1=PhotoImage(file="images/send-50.png")
    window.iconphoto(False,image_icon1)

    Sbackground=PhotoImage(file="images/sender.png")
    Label(window,image=Sbackground).place(x=-2,y=0)

    Mbackground=PhotoImage(file="images/id.png")
    Label(window,image=Mbackground,bg=("#f4fdfe")).place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f'ID:{host}',bg='white',fg='black').place(x=140,y=290)

    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file).place(x=160, y=150)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg="#000",fg="#fff",command=sender).place(x=300,y=150)

    window.mainloop()

def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)


    #icon
    image_icon1 = PhotoImage(file="images/ireceive-64.png")
    main.iconphoto(False,image_icon1)

    main.mainloop()

#icon
image_icon=PhotoImage(file="images/file-64.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer",font=('Acumin Variable Concept',20,'bold'),bg="#f4fdfe").place(x=20,y=30)
Frame(root,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="images/send-50.png")
send=Button(root,image=send_image,bg="#f4fdfe",bd=0,command=Send)
send.place(x=50,y=100)

receive_image=PhotoImage(file="images/ireceive-64.png")
receive=Button(root,image=receive_image,bg="#f4fdfe",bd=0)
receive.place(x=300,y=100)

#label
Label(root,text="Send",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=65,y=200)
Label(root,text="Receive",font=('Acumin Variable Concept',17,'bold'),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="images/Background.png")
Label(root,image=background).place(x=-2,y=280)





root.mainloop()



