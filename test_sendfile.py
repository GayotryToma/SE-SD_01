import io
import pytest
from unittest.mock import MagicMock
from model import FileTransferModel


class TestSendFile:
    def test_send_file_successful(self, mocker):
        # Mock the socket and file
        mock_socket = MagicMock()
        mock_connection = MagicMock()
        mock_file = io.BytesIO(b"file_data")  # Using BytesIO to create a file-like object

        # Set up mock behaviors
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.accept.return_value = (mock_connection, ("dummy_address",))

        # Create an instance of FileTransferModel
        obj = FileTransferModel()

        # Patch the socket.socket method to return the mock socket
        mocker.patch("socket.socket", return_value=mock_socket_instance)

        # Call the send_file method
        obj.send_file("test.txt", mock_file)

    def test_send_file_no_data(self, mocker):
        # Mock the socket and file
        mock_socket = MagicMock()
        mock_connection = MagicMock()
        mock_file = io.BytesIO(b"")  # Using BytesIO to create a file-like object with empty data

        # Set up mock behaviors
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.accept.return_value = (mock_connection, ("dummy_address",))

        # Create an instance of FileTransferModel
        obj = FileTransferModel()

        # Patch the socket.socket method to return the mock socket
        mocker.patch("socket.socket", return_value=mock_socket_instance)

        # Call the send_file method
        obj.send_file("test.txt", mock_file)
