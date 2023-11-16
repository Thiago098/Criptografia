print("Bem vindo! \nCrie sua senha no TechCreators!")
print("---" * 23)
print("\n          ----- AVISO -----\n*** SENHA PERMITE QUALQUER CARACTER ***\n")
senha_inicio = str(input("Digite sua senha: "))
senha_conf = str(input("Confirme sua senha: "))

while (senha_inicio != senha_conf):
    print("Confirmação invalida!")
    print("---" * 23)
    senha_conf = str(input("Confirme sua senha: "))
    
print("Confirmação valida!")
print("---" * 23)
print("---" * 23)

print("\nAgora vamos criptografar sua senha!")

def xor_encrypt(text, key):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(text, key * (len(text) // len(key)) + key[: len(text) % len(key)]))

def criar_senha():
    senha = senha_inicio
    chave = input("Digite a chave para criptografia da senha: ")
    senha_cifrada = xor_encrypt(senha, chave)
    return senha_cifrada, chave

def descriptografar_senha(senha_cifrada, chave):
    senha = xor_encrypt(senha_cifrada, chave)
    return senha


senha_cifrada, chave = criar_senha()
print(f".\n ---- Sua senha foi criada com sucesso! ----\nSenha Cifrada: {senha_cifrada}")
print("---" * 23)


acao = input("\nDigite 'c' para codificar uma nova chave ou\n'd' para descriptografar a senha atual: ").lower()

if acao == 'c':
    print("---- REGISTRE UMA NOVA CHAVE! ----")
    senha_cifrada, chave = criar_senha()
    print(f".\n ---- Chave registrada com sucesso! ----\nNova senha Cifrada: {senha_cifrada}")
    print("\nObrigado por utilizar nosso sistema! <3")
elif acao == 'd':
    print("---- DIGITE A SENHA CRIPTOGRAFADA! ----")
    senha_tentativa = input("Validar e descriptografar: ")
    senha = descriptografar_senha(senha_tentativa, chave)
    print(f".\n ---- Senha descriptografada com sucesso! ----\nSenha Descriptografada: {senha}")
    print("\nObrigado por utilizar nosso sistema! <3")
else:
    print("---" * 23)
    print("\nInfelizmente está ação é inválida!\nExecute o programa novamente e digite 'c' ou 'd'.")
