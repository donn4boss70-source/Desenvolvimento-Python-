# Solicitando o número para o usuário
numero = int(input("Digite um número para ver as quatro tabuadas: "))

# --- ADIÇÃO ---
print(f"\n--- Tabuada de Adição (+) do {numero} ---")
for i in range(1, 11):
    resultado = numero + i
    print(f"{numero} + {i} = {resultado}")

# --- SUBTRAÇÃO ---
print(f"\n--- Tabuada de Subtração (-) do {numero} ---")
for i in range(1, 11):
    # Dica: começamos do próprio número para não dar resultado negativo na tabuada padrão
    resultado = (numero + i) - numero
    print(f"{numero + i} - {numero} = {i}")

# --- MULTIPLICAÇÃO ---
print(f"\n--- Tabuada de Multiplicação (x) do {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# --- DIVISÃO ---
print(f"\n--- Tabuada de Divisão (/) do {numero} ---")
for i in range(1, 11):
    # Multiplicamos antes para garantir que a divisão seja exata e inteira
    dividendo = numero * i
    resultado = dividendo // numero  # Usamos '//' para o resultado vir redondo (inteiro)
    print(f"{dividendo} : {numero} = {resultado}")

print("\n-----------------------------------------")