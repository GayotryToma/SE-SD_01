# Define Constants
LOGIN_WINDOW_WIDTH = 600
LOGIN_WINDOW_HEIGHT = 470
MAIN_WINDOW_WIDTH = 450
MAIN_WINDOW_HEIGHT = 560
BUTTON_WIDTH = 130
BUTTON_HEIGHT = 50
SEND_BUTTON_X = 50
SEND_BUTTON_Y = 100
RECEIVE_BUTTON_X = 300
RECEIVE_BUTTON_Y = 100
SEND_LABEL_X = 65
SEND_LABEL_Y = 200
RECEIVE_LABEL_X = 300
RECEIVE_LABEL_Y = 200
BACKGROUND_IMAGE_X = -2
BACKGROUND_IMAGE_Y = 280
ARROW_BUTTON_WIDTH = 130
ARROW_BUTTON_HEIGHT = 50
ARROW_BUTTON_X = 20
ARROW_BUTTON_Y = 500


# view.py
from tkinter import Tk, Button, Entry, Label, PhotoImage, Toplevel, filedialog, StringVar, IntVar, Checkbutton, LEFT
import os
from model import FileTransferModel
import socket
from tkinter import messagebox
from tkinter import ttk

class FileTransferView:
    EMAIL_LABEL_X_POS = 100
    EMAIL_LABEL_Y_POS = 200
    PASSWORD_LABEL_X_POS = 100
    PASSWORD_LABEL_Y_POS = 250
    EMAIL_ENTRY_X_POS = 200
    EMAIL_ENTRY_Y_POS = 200
    PASSWORD_ENTRY_X_POS = 200
    PASSWORD_ENTRY_Y_POS = 250
    CHECKBOX_X_POS = 200
    CHECKBOX_Y_POS = 300
    LOGIN_BUTTON_X_POS = 250
    LOGIN_BUTTON_Y_POS = 380
    def __init__(self, mode="Login", controller=None, filedialog_module=filedialog):
        self.filedialog = filedialog_module
        self.root = Tk()
        self.mode = mode
        self.controller = controller
        self.root.title("FileEDroP" if mode == "Main" else "Login")
        self.root.geometry(f"{LOGIN_WINDOW_WIDTH}x{LOGIN_WINDOW_HEIGHT}" if mode == "Login" else f"{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}")
        self.root.configure(bg="#f4fdfe")
        self.root.resizable(False, False)

        if mode == "Login":
            self.emailValue = StringVar()
            self.passValue = StringVar()
            self.checkValue = IntVar()

            Label(self.root, text="Login your account", font="arial 25").pack(pady=50)

            Label(self.root, text="Email", font=23).place(x=self.EMAIL_LABEL_X_POS, y=self.EMAIL_LABEL_Y_POS)
            Label(self.root, text="Password", font=23).place(x=self.PASSWORD_LABEL_X_POS, y=self.PASSWORD_LABEL_Y_POS)

            self.emailEntry = Entry(self.root, textvariable=self.emailValue, width=30, bd=2, font=20)
            self.passEntry = Entry(self.root, textvariable=self.passValue, width=30, bd=2, font=20, show="*")
            self.emailEntry.place(x=self.EMAIL_ENTRY_X_POS, y=self.EMAIL_ENTRY_Y_POS)
            self.passEntry.place(x=self.PASSWORD_ENTRY_X_POS, y=self.PASSWORD_ENTRY_Y_POS)

            self.checkbtn = Checkbutton(self.root, text="Remember me?", variable=self.checkValue)
            self.checkbtn.place(x=self.CHECKBOX_X_POS, y=self.CHECKBOX_Y_POS)

            self.login_button = Button(self.root, text="Login", font=20, width=11, height=2, command=self.login)
            self.login_button.place(x=self.LOGIN_BUTTON_X_POS, y=self.LOGIN_BUTTON_Y_POS)
        elif mode == "Main":
            self.root.title("FileEDroP")
            self.root.geometry(f"{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}+500+200")
            self.root.configure(bg="#f4fdfe")
            self.root.resizable(False, False)

            image_icon = PhotoImage(file="images/file-64.png")
            self.root.iconphoto(False, image_icon)

            self.send_button_img = PhotoImage(file="images/send-50.png")
            self.send_button = Button(self.root, image=self.send_button_img, bg="#f4fdfe", bd=0, command=self.on_send_button_click)
            self.send_button.place(x=SEND_BUTTON_X, y=SEND_BUTTON_Y)

            self.receive_button_img = PhotoImage(file="images/ireceive-64.png")
            self.receive_button = Button(self.root, image=self.receive_button_img, bg="#f4fdfe", bd=0, command=self.on_receive_button_click)
            self.receive_button.place(x=RECEIVE_BUTTON_X, y=RECEIVE_BUTTON_Y)

            self.send_label = Label(self.root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
            self.send_label.place(x=SEND_LABEL_X, y=SEND_LABEL_Y)

            self.receive_label = Label(self.root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe")
            self.receive_label.place(x=RECEIVE_LABEL_X, y=RECEIVE_LABEL_Y)

            self.background_img = PhotoImage(file="images/Background.png")
            self.background_label = Label(self.root, image=self.background_img)
            self.background_label.place(x=BACKGROUND_IMAGE_X, y=BACKGROUND_IMAGE_Y)

    def on_send_button_click(self):
        send_view = SendView(self.root, FileTransferModel())  # Pass FileTransferModel instance to SendView

    def on_receive_button_click(self):
        receive_view = ReceiveView(self.root, FileTransferModel())  # Pass FileTransferModel instance to ReceiveView

    def login(self):
        email = self.emailValue.get()
        password = self.passValue.get()
        remember_me = self.checkValue.get()

        if email and password:
            print("Login successful")
            if remember_me:
                print("Remember me checked")
            else:
                print("Remember me not checked")
            if self.controller:
                self.controller.handle_login_sucess()
        else:
            print("Login failed")

    def run(self):
        self.root.mainloop()

    class SendView:
        WINDOW_WIDTH = 450
        WINDOW_HEIGHT = 560
        WINDOW_X_POS = 500
        WINDOW_Y_POS = 200
        BACKGROUND_IMAGE_X_POS = -2
        BACKGROUND_IMAGE_Y_POS = 0
        LOGO_X_POS = 10
        LOGO_Y_POS = 250
        SELECT_FILE_BUTTON_X_POS = 160
        SELECT_FILE_BUTTON_Y_POS = 150
        SEND_BUTTON_X_POS = 300
        SEND_BUTTON_Y_POS = 150
        PROGRESSBAR_X_POS = 75
        PROGRESSBAR_Y_POS = 200

        def __init__(self, parent, model, filedialog_module=filedialog):
            self.filedialog = filedialog_module
            self.parent = parent
            self.model = model
            self.filename = None
            self.window = Toplevel(parent)
            self.window.title("Send")
            self.window.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{self.WINDOW_X_POS}+{self.WINDOW_Y_POS}")
            self.window.configure(bg="#f4fdfe")
            self.window.resizable(False, False)

            self.Sbackground = PhotoImage(file="images/sender.png")
            background_label = Label(self.window, image=self.Sbackground)
            background_label.place(x=self.BACKGROUND_IMAGE_X_POS, y=self.BACKGROUND_IMAGE_Y_POS)

            self.Mbackground = PhotoImage(file="images/id.png")
            label_image = Label(self.window, image=self.Mbackground, bg="#f4fdfe")
            label_image.place(x=self.LOGO_X_POS, y=self.LOGO_Y_POS)

            host = socket.gethostname()
            self.host_label = Label(self.window, text=f'ID: {host}', bg='white', fg='black', font='arial 14')
            self.host_label.place(x=self.LOGO_X_POS + 30, y=self.LOGO_Y_POS + 30)

            self.select_file_button = Button(self.window, text="+ select file", width=10, height=1,
                                             font=('arial', 14, 'bold'), bg="#f4fdfe", bd=0, command=self.select_file)
            self.select_file_button.place(x=self.SELECT_FILE_BUTTON_X_POS, y=self.SELECT_FILE_BUTTON_Y_POS)

            self.send_button = Button(self.window, text="Send", width=8, height=1, font=('arial', 14, 'bold'),
                                      bg="#f4fdfe", bd=0, command=self.send_file_wrapper)
            self.send_button.place(x=self.SEND_BUTTON_X_POS, y=self.SEND_BUTTON_Y_POS)

            self.progressbar = ttk.Progressbar(self.window, orient="horizontal", length=300, mode="determinate")
            self.progressbar.place(x=self.PROGRESSBAR_X_POS, y=self.PROGRESSBAR_Y_POS)

    def select_file(self):
        filename = self.filedialog.askopenfilename(parent=self.window, initialdir=os.getcwd(),
                                                    title='Select File',
                                                    filetype=(('file type', '*.txt'), ('all files', '*.*')))
        if filename:
            self.filename = filename
            print("Selected file path:", self.filename)
            return filename
        else:
            return None

    def send_file_wrapper(self):
        if self.filename:
            with open(self.filename, 'rb') as file:
                file_data = file.read()

                total_length = len(file_data)
                CHUNK_SIZE = 1024
                num_chunks = total_length // CHUNK_SIZE
                for i in range(num_chunks + 1):
                    start = i * CHUNK_SIZE
                    end = min((i + 1) * CHUNK_SIZE, total_length)
                    self.progressbar["value"] = (end / total_length) * 100
                    self.progressbar.update_idletasks()

                    chunk_data = file_data[start:end]

                    self.model.send_file(self.filename, file_data, chunk_data)

            messagebox.showinfo("Success", "Data has been transmitted successfully.")
        else:
            messagebox.showinfo("No file selected", "Please select a file.")

class ReceiveView:
    WINDOW_WIDTH = 450
    WINDOW_HEIGHT = 560
    WINDOW_X_POS = 500
    WINDOW_Y_POS = 200
    BACKGROUND_IMAGE_X_POS = -2
    BACKGROUND_IMAGE_Y_POS = 0
    LOGO_X_POS = 10
    LOGO_Y_POS = 250
    SENDER_ID_LABEL_X_POS = 20
    SENDER_ID_LABEL_Y_POS = 340
    SENDER_ID_ENTRY_X_POS = 20
    SENDER_ID_ENTRY_Y_POS = 370
    FILENAME_LABEL_X_POS = 20
    FILENAME_LABEL_Y_POS = 420
    FILENAME_ENTRY_X_POS = 20
    FILENAME_ENTRY_Y_POS = 450

    def __init__(self, parent, model):
        self.parent = parent
        self.model = model
        self.main = Toplevel(parent)
        self.main.title("Receive")
        self.main.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}+{self.WINDOW_X_POS}+{self.WINDOW_Y_POS}")
        self.main.configure(bg="#f4fdfe")
        self.main.resizable(False, False)

        self.Hbackground = PhotoImage(file="images/receiver.png")
        background_label = Label(self.main, image=self.Hbackground)
        background_label.place(x=self.BACKGROUND_IMAGE_X_POS, y=self.BACKGROUND_IMAGE_Y_POS)

        self.logo = PhotoImage(file='images/profile.png')
        logo_label = Label(self.main, image=self.logo, bg="#f4fdfe")
        logo_label.place(x=self.LOGO_X_POS, y=self.LOGO_Y_POS)

        self.sender_id_label = Label(self.main, text="Input Sender ID", font=('arial', 10, 'bold'), bg="#f4fdfe")
        self.sender_id_label.place(x=self.SENDER_ID_LABEL_X_POS, y=self.SENDER_ID_LABEL_Y_POS)

        self.sender_id_entry = Entry(self.main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
        self.sender_id_entry.place(x=self.SENDER_ID_ENTRY_X_POS, y=self.SENDER_ID_ENTRY_Y_POS)
        self.sender_id_entry.focus()

        self.filename_label = Label(self.main, text="Filename for the Incoming File:", font=('arial', 10, 'bold'),
                                    bg="#f4fdfe")
        self.filename_label.place(x=self.FILENAME_LABEL_X_POS, y=self.FILENAME_LABEL_Y_POS)

        self.filename_entry = Entry(self.main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
        self.filename_entry.place(x=self.FILENAME_ENTRY_X_POS, y=self.FILENAME_ENTRY_Y_POS)
        imageicon = PhotoImage(file="images/arrow.png")
        receive_button = Button(self.main, text="Receive", compound=LEFT, image=imageicon, width=ARROW_BUTTON_WIDTH, height=ARROW_BUTTON_HEIGHT, bg="#39c790",
                                font="arial 14 bold", command=self.receive_file)
        receive_button.image = imageicon
        receive_button.place(x=ARROW_BUTTON_X, y=ARROW_BUTTON_Y)

    def receive_file(self):
        sender_id = self.sender_id_entry.get()
        filename = self.filename_entry.get()
        self.model.receive_file(sender_id, filename)
if __name__ == "__main__":
    view = FileTransferView()
    view.run()
