import pytest
from model import FileTransferModel
import socket

class TestReceiveFile:
    def setup_method(self, method):
        self.obj = FileTransferModel()  # Initialize your class instance

    def test_receive_file_successful(self, mocker):
        sender_id = "192.168.1.100"
        filename = "received_data.txt"
        expected_output = "File has been received successfully"

        # Mock the socket connection

        mock_socket_instance = mocker.MagicMock()
        mock_socket_instance.recv.side_effect = [b'data_chunk1', b'data_chunk2', b'']  # Simulate receiving data
        mock_socket_instance.connect.return_value = None
        mocker.patch('socket.socket', return_value=mock_socket_instance)

        # Call the method
        result=self.obj.receive_file(sender_id, filename)

        # Check if the result matches the expected output
        assert result == expected_output


    def test_receive_file_error(self, mocker):
        sender_id = "invalid_ip"
        filename = "received_data.txt"
        expected_error = f"Error connecting to {sender_id}:[error message]"

        # Mock the socket connection to raise an error

        mock_socket_instance = mocker.MagicMock()
        mock_socket_instance.connect.side_effect = socket.error("[error message]")  # Simulate socket connection error
        mocker.patch('socket.socket', return_value=mock_socket_instance)

        # Call the method
        result=self.obj.receive_file(sender_id, filename)

        # Check if the result matches the expected error message
        assert result.strip()==expected_error.strip()

        # Print the values of result and expected_error for debugging
        print("Result:", repr(result))
        print("Expected error:", repr(expected_error))