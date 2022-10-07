from datetime import datetime


def convert_to_string(data):
    return datetime.strptime(data, '%d/%m/%Y').date()
