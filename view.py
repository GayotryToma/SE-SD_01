# view.py
from tkinter import Tk,Button, Entry, Label, PhotoImage, Toplevel, filedialog,LEFT
import os
from model import FileTransferModel
import socket
from tkinter import messagebox
from tkinter import ttk

class FileTransferView:
    def __init__(self):
        self.root = Tk()
        self.root.title("FileEDroP")
        self.root.geometry("450x560+500+200")
        self.root.configure(bg="#f4fdfe")
        self.root.resizable(False, False)

        image_icon = PhotoImage(file="images/file-64.png")
        self.root.iconphoto(False, image_icon)

        self.send_button_img = PhotoImage(file="images/send-50.png")
        self.send_button = Button(self.root, image=self.send_button_img, bg="#f4fdfe", bd=0, command=self.on_send_button_click)
        self.send_button.place(x=50, y=100)

        self.receive_button_img = PhotoImage(file="images/ireceive-64.png")
        self.receive_button = Button(self.root, image=self.receive_button_img, bg="#f4fdfe", bd=0, command=self.on_receive_button_click)
        self.receive_button.place(x=300, y=100)

        self.send_label = Label(self.root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
        self.send_label.place(x=65, y=200)

        self.receive_label = Label(self.root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
        self.receive_label.place(x=300, y=200)

        self.background_img = PhotoImage(file="images/Background.png")
        self.background_label = Label(self.root, image=self.background_img)
        self.background_label.place(x=-2, y=280)

    def on_send_button_click(self):
        send_view = SendView(self.root, FileTransferModel())  # Pass FileTransferModel instance to SendView

    def on_receive_button_click(self):
        receive_view = ReceiveView(self.root, FileTransferModel())  # Pass FileTransferModel instance to ReceiveView

    def run(self):
        self.root.mainloop()

class SendView:
    def __init__(self, parent, model):
        self.parent = parent
        self.model = model # Store FileTransferModel instance
        self.filename=None
        self.window = Toplevel(parent)
        self.window.title("Send")
        self.window.geometry('450x560+500+200')
        self.window.configure(bg="#f4fdfe")
        self.window.resizable(False, False)


        self.Sbackground = PhotoImage(file="images/sender.png")#Sbackground indicates sender image in send window

        background_label = Label(self.window, image=self.Sbackground)
        background_label.place(x=-2, y=0)

        self.Mbackground = PhotoImage(file="images/id.png")#Mbackground indicates id-image in send window
        label_image = Label(self.window, image=self.Mbackground, bg="#f4fdfe")
        label_image.place(x=100, y=260)

        host = socket.gethostname()
        self.host_label = Label(self.window, text=f'ID: {host}', bg='white', fg='black', font='arial 14')
        self.host_label.place(x=140, y=290)

        self.select_file_button = Button(self.window,text="+ select file" ,width=10,height=1,font=('arial', 14, 'bold'), bg="#f4fdfe", bd=0, command=self.select_file)
        self.select_file_button.place(x=160, y=150)


        self.send_button = Button(self.window, text="Send",width=8,height=1 ,font=('arial', 14, 'bold'),bg="#f4fdfe", bd=0, command=self.send_file)
        self.send_button.place(x=300, y=150)

        self.progressbar=ttk.Progressbar(self.window,orient="horizontal",length=300,mode="determinate")
        self.progressbar.place(x=75,y=200)

    def select_file(self):
        self.filename = filedialog.askopenfilename(parent=self.window,initialdir=os.getcwd(),
                                                   title='Select File',
                                                   filetype=(('file type', '*.txt'), ('all files', '*.*')))

    def send_file(self):
        if self.filename:
            with open(self.filename, 'rb') as file:
                file_data = file.read()  # Read file data

                #Update progress bar while sending file
                total_length= len(file_data)
                CHUNK_SIZE=1024
                num_chunks=total_length// CHUNK_SIZE
                for i in range(num_chunks+1):
                    start = i*CHUNK_SIZE
                    end=min((i+1)*CHUNK_SIZE,total_length)
                    self.progressbar["value"]=(end/total_length)*100
                    self.progressbar.update_idletasks()

                    chunk_data=file_data[start:end]

                    self.model.send_file(self.filename, file_data,chunk_data)  # Pass both filename and file data to the model
            messagebox.showinfo("Success","Data has been transmitted successfully.")
        else:
            messagebox.showinfo("No file selected", "Please select a file.")

class ReceiveView:
    def __init__(self, parent, model):
        self.parent = parent
        self.model = model  # Store FileTransferModel instance
        self.main = Toplevel(parent)
        self.main.title("Receive")
        self.main.geometry('450x560+500+200')
        self.main.configure(bg="#f4fdfe")
        self.main.resizable(False, False)

        # Display the background image
        self. Hbackground = PhotoImage(file="images/receiver.png")
        background_label = Label(self.main, image=self.Hbackground)
        background_label.place(x=-2, y=0)

        # Display the logo image
        self. logo = PhotoImage(file='images/profile.png')
        logo_label = Label(self.main, image=self.logo, bg="#f4fdfe")
        logo_label.place(x=10, y=250)

        self.sender_id_label = Label(self.main, text="Input Sender ID", font=('arial', 10, 'bold'), bg="#f4fdfe")
        self.sender_id_label.place(x=20, y=340)

        self.sender_id_entry = Entry(self.main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
        self.sender_id_entry.place(x=20, y=370)
        self.sender_id_entry.focus()

        self.filename_label = Label(self.main, text="Filename for the Incoming File:", font=('arial', 10, 'bold'), bg="#f4fdfe")
        self.filename_label.place(x=20, y=420)

        self.filename_entry = Entry(self.main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
        self.filename_entry.place(x=20, y=450)

        imageicon = PhotoImage(file="images/arrow.png")
        receive_button = Button(self.main, text="Receive", compound=LEFT, image=imageicon, width=130, bg="#39c790",
                                font="arial 14 bold", command=self.receive_file)
        receive_button.image = imageicon  # Keep a reference to the image to prevent garbage collection
        receive_button.place(x=20, y=500)



    def receive_file(self):
        sender_id = self.sender_id_entry.get()
        filename = self.filename_entry.get()
        self.model.receive_file(sender_id, filename)  # Use existing FileTransferModel instance
