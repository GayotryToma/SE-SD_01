# controller.py
from tkinter import Tk
from view import FileTransferView
from model import FileTransferModel


class FileTransferController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.controller=self
        self.view.login_button.config(command=self.login)
        #self.view.select_file_button.config(command=self.select_file)
        self.view.run()
        self.main_view =None


    #def select_file(self):
        # Implement file selection logic here
        #filename = self.view.select_file()
        #if filename:
            #print("Selected file:", filename)
            # Optionally, you can update the view with the selected filename
    def handle_login_success(self):
        print("handling login success")
        self.main_view= FileTransferView(mode="Main")
        self.main_view.controller=self
    def login(self):
        email=self.view.emailValue.get()
        password=self.view.passValue.get()
        remember_me= self.view.checkValue.get()

        if email and password:
            print("Login successful")
            if remember_me:
                print("Remember me checked")
            else:
                print("Remember me not checked")
            self.view.root.destroy()  # Close the login window
            self.handle_login_success()
        else:
            print("Login failed ")


if __name__ == "__main__":
    model = FileTransferModel()
    login_view = FileTransferView()
    login_controller = FileTransferController(login_view, model)
