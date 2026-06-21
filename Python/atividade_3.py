# Dados sujos 
nomes_sujos = [
    "jOãO-sIlVa",
    "mArIa-fErNaNdA-sOuZa",
    "cArLoS-eDuArDo-oLiVeIrA",
    "aNa-cLaRa-mEnDoNçA",
    "lUcAs-pErEiRa-liMa",
    "bEaTrIz-cOsTA-sAnToS",
    "gUiLhErMe-aLvEs",
    "jULiAnA-rAmOs-fReItAs",
    "pEdRo-hEnRiQuE-nAsciMeNtO",
    "lArIsSa-mOuRa-cAmPoS",
]

nomes_sujos.append(input("Digite o Nome Completo:"))
print(nomes_sujos)

# Passo 2: Higienização
nomes_limpos = []
for nome in nomes_sujos:
    nomes_limpos.append(nome.replace("-", " ").title())

print('NOMES LIMPOS AQUI EMBAIXO','\n', nomes_limpos)

# Passo 3: Padronização
nome_padronizado = []
for nome in nomes_limpos:
    nome_padronizado.append(nome.upper())

print('NOMES PADRONIZADOS AQUI EMBAIXO','\n',nome_padronizado)

tamanho = len(nome_padronizado)
print(f"Tamanho da lista de nomes padronizados: {tamanho}")
print(f"Entrada: {nomes_sujos}|")
for nome in nome_padronizado:
    print(f"Crachá: {nome} | Caracteres: {len(nome)}")
print("-" * 40)