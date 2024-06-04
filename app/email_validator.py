# fichier: email_validator.py

import re

def is_valid_email(email):
    """ Valide si l'adresse e-mail donnée est conforme à un pattern simple. """
    if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return True
    else:
        return False
