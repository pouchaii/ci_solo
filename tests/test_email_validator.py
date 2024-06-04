# fichier: test_email_validator.py

from app.email_validator import is_valid_email

def test_valid_email():
    """ Teste des adresses e-mail qui devraient être valides. """
    assert is_valid_email("example@example.com")
    assert is_valid_email("user.name@domain.co.in")
    assert is_valid_email("first-last@domain.org")
    assert is_valid_email("12é3434@gmail.com")

def test_invalid_email():
    """ Teste des adresses e-mail qui ne devraient pas être valides. """
    assert not is_valid_email("plainaddress")
    assert not is_valid_email("missingatsign.com")
    assert not is_valid_email("invalid@domain@domain.com")
    assert not is_valid_email("@missingusername.com")
    assert not is_valid_email("&2&é&@gmail.com")