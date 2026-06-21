# Dados sujos 
nomes_sujos = [
    "MARIA ROSÁRIO DE FÁTIMA DUARTE FERREIRA", 
    "GABRIEL CARNEIRO BARROS",
    "LUIZ AUGUSTO XAVIER DE OLIVEIRA",
    "SEVERINO ITAMAR DA SILVA",
    "AMANDA CARDOSO RIBEIRO",
    "GABRIEL ALVES SABIA",
    "JULIANA BARBOSA FERREIRA",
    "ALEXANDRO HEITOR DOS SANTOS FERREIRA",
    "PEDRO CALDAS DE FARIAS",
    "GABRIELLA CUNHA MACIEL",
    "JULIO CESAR SOUZA RODRIGUES DOS SANTOS",
    "MIGUEL GUILHERME ALVES RODRIGUES",
    "LARA LORRANY GUEDES DIAS",
    "ALONSO DOS SANTOS SILVA",
    "PAULO VICTOR HAHN SIQUEIRA",
    "JESSICA CRISTINA GOMES PIMENTA DE OLIVEIRA",
    "DANIELLE MONTEIRO BRITO",
    "CARLOS HENRIQUE FELIX DA SILVA",
    "GABRIEL ANDRÉ DA SILVEIRA SILVA",
    "MIGUEL VÍTOR MENDES DA SILVA",
    "GUILHERME FEITOSA RODRIGUES DA SILVA",
    "MARIA LUIZA OLIVEIRA DE SÁ",
    "FRANCIELE MARIA FERREIRA",
    "ÁLEF CALEB AZEVEDO BRITO",
    "JOÃO FELLYPE ROCHA SANTANA",
    "PEDRO HENRIQUE ALVES BARBOSA RIBEIRO LEANDRO",
    "GILVANIR DOS SANTOS DE SOUSA",
    "GABRIEL EVANGELISTA SILVA",
]

nomes_sujos.append(input("Digite o Nome Completo:"))
print(nomes_sujos)

# Passo 2: Higienização
nomes_limpos = []
for nome in nomes_sujos:
    nomes_limpos.append(nome.replace("-", " ").title())

print('NOMES LIMPOS AQUI EMBAIXO','\n', nomes_limpos)

tamanho = len(nomes_limpos)
print(f"Tamanho da lista de nomes padronizados: {tamanho}")
print(f"Entrada: {nomes_sujos}|")
for nome in nomes_limpos:
    print(f"Crachá: {nome} | Caracteres: {len(nome)}")
print("-" * 40)