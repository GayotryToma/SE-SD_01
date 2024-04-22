from unittest.mock import MagicMock
from controller import  FileTransferController  # Import YourClass from your module

class TestLoginSuccess:
    def setup_method(self):
        # Mock the view's attributes and methods
        view = MagicMock()
        view.emailValue.get.return_value = "example@example.com"
        view.passValue.get.return_value = "password123"
        view.checkValue.get.return_value = True

        model = MagicMock()  # Mock the model
        self.obj = FileTransferController(view, model)

    def test_login_successful_remember_me_checked(self):
        # Call the login method
        self.obj.login()

        # Assert that login was successful
        assert self.obj.view.root.destroy.called
        assert self.obj.main_view.mode == "Main"

class TestLoginFailure:
    def setup_method(self):
        # Mock the view's attributes and methods
        view = MagicMock()
        view.emailValue.get.return_value = ""  # Empty email
        view.passValue.get.return_value = ""  # Empty password
        view.checkValue.get.return_value = False  # Remember me not checked

        model = MagicMock()  # Mock the model
        self.obj = FileTransferController(view, model)

    def test_login_failed(self):
        # Call the login method
        self.obj.login()

        # Assert that login failed
        assert not self.obj.view.root.destroy.called
        assert self.obj.main_view is None
