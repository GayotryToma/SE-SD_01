import socket
from tkinter import filedialog,Tk
import os

class FileTransferModel:
    CHUNK_SIZE = 1024# Adjust chunk size according to needs
    PORT=8080

    def select_file(self):
        root=Tk()
        root.withdraw() #hide the main window

        file_path=filedialog.askopenfilename(title="Select File To Send")
        print("Selected file path:",file_path)
        root.destroy()
        return file_path

    def send_file(self,filename,file_data,chunk_data=None):

        s=socket.socket()
        host=socket.gethostname()
        s.bind((host,self.PORT))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections...')
        conn,addr=s.accept()
        conn.sendall(file_data)


        #with open(filename,'wb') as file:
                #conn.sendall(file_data.getvalue())
        if chunk_data:
            conn.sendall(chunk_data)
        print("Data has been transmitted successfully")

    def receive_file(self,sender_id,filename):
        result_message=""
        try:

           s=socket.socket()
           s.connect((sender_id,self.PORT))
        except socket.error as e:
            result_message=(f"Error connecting to {sender_id}:{e}")
            print(result_message)
            return result_message


        with open(filename,'wb') as file:
            while True:
                file_data=s.recv(self.CHUNK_SIZE)
                if not file_data:
                    break
                file.write(file_data)

        result_message = "File has been received successfully"
        print(result_message)  # Print the success message
        return result_message



if __name__ == "__main__":
   model = FileTransferModel()
   filename=model.select_file()
   if filename:
       with open(filename,'rb') as file:
           file_data=file.read()
           model.send_file(filename,file_data)





