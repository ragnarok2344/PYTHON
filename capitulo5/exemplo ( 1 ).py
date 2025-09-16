def validalogin(nome,senha):
   if (nome == "felipe" and senha =="senha123"):
      return print("seja bem vindo",nome,senha)
   else:
       return print("senha ou login invalidos")
print("=== Digite seu nome ===")
nome=input()
print("=== digite sua senha ===")
senha = input()

validalogin(nome, senha)
