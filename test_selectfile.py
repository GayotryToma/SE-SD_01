import pytest
from unittest.mock import MagicMock
from view import SendView

class TestSelectFile:
    def setup_method(self):
        # Mock the necessary modules and objects
        self.mock_tkinter = MagicMock()
        self.mock_tkinter.filedialog.askopenfilename.return_value = "test.txt"

    def test_select_file_successful(self):
        # Create an instance of SendView with the mocked filedialog module
        send_view = SendView(None, None, self.mock_tkinter.filedialog)

        # Call the select_file method
        filename = send_view.select_file()

        # Assert that the filename is set correctly
        assert filename == "test.txt"

    def test_select_file_cancel(self):
        # Create an instance of SendView with the mocked filedialog module
        send_view = SendView(None, None, self.mock_tkinter.filedialog)

        # Mock the askopenfilename method to return an empty string, simulating canceling the dialog
        self.mock_tkinter.filedialog.askopenfilename.return_value = ""

        # Call the select_file method
        filename = send_view.select_file()

        # Assert that the filename is None when the dialog is canceled
        assert filename is None

if __name__ == "__main__":
    pytest.main()
