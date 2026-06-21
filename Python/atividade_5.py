# Dicionário dos Estudantes 
estudantes = [
    {"nome": "Ana Clara Souza",        "nota": 10.0},
    {"nome": "Bruno Henrique Lima",    "nota": 10.0},
    {"nome": "Carla Mendonça",         "nota": 10.0},
    {"nome": "Diego Ferreira",         "nota": 10.0},
    {"nome": "Eduarda Ramos",          "nota": 6.0},
    {"nome": "Felipe Oliveira",        "nota": 6.0},
    {"nome": "Gabriela Costa",         "nota": 6.0},
    {"nome": "Henrique Alves",         "nota": 2.0},  
    {"nome": "Isabela Moura",          "nota": 4.5},
    {"nome": "João Pedro Nascimento",  "nota": 6.0},
]
# Cabeçalho 
print("=" * 50)
print("       BOLETIM FINAL - TURMA 2025")
print("=" * 50)

# Leitura do Dicionário
for estudante in estudantes:
    nome = estudante["nome"]
    nota = estudante["nota"]
    # Estudantes APROVADOS 
    if nota >= 6:
        situacao = "🟢  Aprovado"
        print(f"{nome}: {situacao} | Nota: {nota}")
    # Estudantes REPROVADOS
    else:
        situacao = "🔴  Reprovado"
        print(f"{nome}: {situacao} | Nota: {nota}")
        # Estudantes de RECUPERAÇÃO
        if nota >= 4.5:
            situacao = "🟡  Em Recuperação"
            print(f"{nome}: {situacao} | Nota: {nota}")