# 1. Importando o módulo necessário para sorteios
import random

# 2. Criando a função que funciona como a nossa "mini-fábrica" de sorteio
def rolar_dado():
    # Sorteia um número inteiro entre 1 e 6 (inclusive)
    numero_sorteado = random.randint(1, 6)
    # Devolve o número para quem chamou a função
    return numero_sorteado

# 3. Programa Principal
print("=== BEM-VINDO AO SIMULADOR DE DADOS ===")

while True:
    # Pergunta a ação do usuário e padroniza para letras minúsculas
    opcao = input("\nDigite 'jogar' para rolar o dado ou 'sair' para encerrar: ").lower()
    
    if opcao == 'sair':
        print("Obrigado por jogar! Boa sorte no Provão de Códigos! 🚀")
        break  # Freio de emergência: encerra o laço while
        
    elif opcao == 'jogar':
        # Chamamos a função e guardamos o resultado que ela "retornou"
        resultado = rolar_dado()
        print(f"🎲 O dado rolou e caiu no número: {resultado}")
        
    else:
        print("Opção inválida! Digite 'jogar' ou 'sair'.")