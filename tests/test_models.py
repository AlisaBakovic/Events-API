import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from models import User


def test_user_password_hashing_behaves_correctly():
    user = User()

    user.set_password("mypassword123")

    assert user.password_hash != "mypassword123"

    assert user.check_password("mypassword123") is True

    assert user.check_password("wrong_password") is False