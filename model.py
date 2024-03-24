import socket
from tkinter import filedialog,Tk
import os

class FileTransferModel:
    CHUNK_SIZE = 10485760# Adjust chunk size according to needs
    PORT=8080

    def select_file(self):
        root=Tk()
        root.withdraw() #hide the main window

        file_path=filedialog.askopenfilename(title="Select File To Send")
        print("Selected file path:",file_path)
        root.destroy()
        return file_path

    def send_file(self,filename,file_data,chunk_data):
       ## filename=self.select_file()
        #if not filename:
         #   print("No file selected.Exiting...")
          #  return

        s=socket.socket()
        host=socket.gethostname()
        s.bind((host,self.PORT))
        s.listen(1)
        print(host)
        print('waiting for any incomig connections...')
        conn,addr=s.accept()


        with open(filename,'wb') as file:
                file.write(file_data)

        print("Data has been transmitted successfully")

    def receive_file(self,sender_id,filename):
        s=socket.socket()
        s.connect((sender_id,self.PORT))


        with open(filename,'wb') as file:
            while True:
                file_data=s.recv(self.CHUNK_SIZE)
                if not file_data:
                    break
                file.write(file_data)

        print("File has been received successfully")

if __name__ == "__main__":
   model = FileTransferModel()
   model.send_file()



