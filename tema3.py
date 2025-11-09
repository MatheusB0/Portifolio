import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    return re.match(padrao, cpf) is not None

def validar_senha(senha):
    padrao = r'^(?=.*[A-Z])(?=.*\d).{6,}$'
    return re.match(padrao, senha) is not None

def validar_data(data):
    padrao = r'^\d{2}/\d{2}/\d{4}$'
    return re.match(padrao, data) is not None