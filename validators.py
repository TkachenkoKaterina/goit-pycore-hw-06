import re

def validate_phone(value):
    return re.fullmatch(r'\d{10}', value) is not None