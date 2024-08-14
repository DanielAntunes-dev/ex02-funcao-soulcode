import re

def senha_segura(senha):
    if len(senha) < 8:
        return "A senha deve ter pelo menos 8 caracteres."

    if not re.search(r'[A-Z]', senha):
        return "A senha deve ter pelo menos uma letra maiúscula."

    if not re.search(r'[a-zA-Z]', senha):
        return "A senha deve ter pelo menos uma letra."

    if not re.search(r'\d', senha):
        return "A senha deve ter pelo menos um número."

    if not re.search(r'[!@#$%^&*]', senha):
        return "A senha deve ter pelo menos um caractere especial (!, @, #, $, %, ^, &, *)."

    return "A senha é segura"

senha = input("Digite a senha: ")
resultado = senha_segura(senha)
print(resultado)
