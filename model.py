import socket


class FileTransferModel:
    CHUNK_SIZE = 10485760  # Adjust chunk size according to needs

    def send_file(self, filename):
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections.... ')
        conn, addr = s.accept()

        with open(filename, 'rb') as file:
            while True:
                file_data = file.read(self.CHUNK_SIZE)
                if not file_data:
                    break  # Reached end of file

                conn.send(file_data)

        print("Data has been transmitted successfully")

    def receive_file(self, sender_id, filename):
        s = socket.socket()
        port = 8080
        s.connect((sender_id, port))

        with open(filename, 'wb') as file:
            while True:
                file_data = s.recv(self.CHUNK_SIZE)
                if not file_data:
                    break  # Reached end of transmission

                file.write(file_data)

        print("File has been received successfully")
