# controller.py
from tkinter import Tk
from view import FileTransferView
from model import FileTransferModel


class FileTransferController:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.run()

if __name__ == "__main__":
    model = FileTransferModel()
    view = FileTransferView()
    controller = FileTransferController(view, model)
