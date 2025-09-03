#############################QUESTÃO 1##############################
sair = ""

while sair.lower() != "sair":
    numeros = []
    print("\nDigite 5 números (ou 'sair' para encerrar):")

    for i in range(5):
        entrada = input(f"Número {i+1}: ")
        if entrada.lower() == "sair":
            sair = "sair"
            break
        numeros.append(int(entrada))

    if sair == "sair":
        print("Programa encerrado.")
        break

    soma = 0
    maior = menor = numeros[0]

    for n in numeros:
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    print(f"\n[f-string] Soma: {soma}, Maior: {maior}, Menor: {menor}")
    print("[format()] Soma: {}, Maior: {}, Menor: {}".format(soma, maior, menor))

################################QUSTÃO 2#####################################

opcao = ""

while opcao.lower() != "sair":
    notas = (7.5, 8.0, 5.0, 9.0, 6.5)

    soma = 0
    for n in notas:
        soma += n
    media = soma / len(notas)

    if media >= 9:
        desempenho = "Excelente"
    elif media >= 7:
        desempenho = "Bom"
    elif media >= 5:
        desempenho = "Regular"
    else:
        desempenho = "Ruim"

    print(f"\n[f-string] Média: {media:.2f} | Desempenho: {desempenho}")

    print("[format()] Média: {:.2f} | Desempenho: {}".format(media, desempenho))

    opcao = input("\nDigite 'sair' para encerrar ou Enter para continuar: ")

print("Programa encerrado.")

###############################QUESTÃO 3###############################


opcao = ''
while opcao.lower() != "sair":
    alunos = {'Ana': 8, 'Joao': 6, 'Pedro': 9}
    print ('\nNota dos alunos:')
    for nome, nota in alunos.items():
        if nota >= 7:
            situacao = 'Aprovado'
        else:
            situacao = 'Reprovado'
        print (f'\n[f-string] {nome}: Nota {nota} - {situacao}')
        print ('[format()] {}: nota {} - {}' .format(nome, nota, situacao))
    opcao = input("\nDigite 'sair' para encerrar ou Enter para continuar: ")
print('Programa encerrado')
 
##############################QUESTÃO 4############################
 
opcao = ''

while opcao.lower() != 'sair':
    palavra = input("\nDigite algo (ou 'sair' para encerrar):")
    if palavra.lower() == 'sair':
        break
    vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    contador = 0

    for letra in palavra.lower():
        if letra in vogais:
            contador +=1
    print (f"[f-string] A palavra '{palavra}' possui {contador} vogais.")
    print ("[format()] A palavra '{}' possui {} vogais. ".format(palavra, contador))
    #opcao = input("\nDigite 'sair' para encerrar ou Enter para continuar: ")
print('Programa encerrado.')

####################QUESTÃO 5#############################

opcao = ''

while opcao.lower() != 'sair':
    numeros = []
    print("\nDigite 2 números (ou 'sair' para encerrar):")
    
    for i in range(2):
        entrada = input(f"Número {i+1}: ")
        if entrada.lower() == "sair":
            opcao = "sair"
            break
        numeros.append(float(entrada))

    if opcao == "sair":
        print("Programa encerrado.")
        break
    
    def operacao():
        soma = numeros[0] + numeros[1]
        print (f'[f-String] A soma entre número {numeros[0]} e {numeros[1]} é = {soma}')
        print ("[format()] A soma entre '{}' e {} é = {} ".format(numeros[0], numeros[1], soma))
        
        sub = numeros[0] - numeros[1]
        print (f'[f-String] A subtração entre número {numeros[0]} e {numeros[1]} é = {sub}')
        print ("[format()] A subtração entre '{}' e {} é = {} ".format(numeros[0], numeros[1], sub))
       
        mult = numeros[0] * numeros[1]
        print (f'[f-String] A multiplicação entre número {numeros[0]} e {numeros[1]} é = {mult}')
        print ("[format()] A multiplicação entre '{}' e {} é = {} ".format(numeros[0], numeros[1], mult))
        
        div = numeros[0] / numeros[1]
        print (f'[f-String] A divisão entre número {numeros[0]} e {numeros[1]} é = {div}')
        print ("[format()] A divisão entre '{}' e {} é = {} ".format(numeros[0], numeros[1], div))
        
    operacao()
    
#################################QUESTÃO 6################################
lista  = []
i = 0
while True:
     
        usuario = input(f"Digite {i+1} usuário(ou 'sair' para encerrar):")
        if usuario.lower() == "sair":
            sair = "sair"
            break
        lista.append(usuario)
        i = i + 1
        
print(f"[f-String] Os usuários são: {lista}")
print("[format()] Os usuários são: {}".format(lista))

#####################QUESTÃO 7###############################

maiuscula = "QWERTYUIOPASDFGHJKLÇZXCVBNM"

contador = 0

digite = input('Digite algo: ')
for x in digite:
    if x in maiuscula:
        contador = contador + 1
print (f"[f-String] Essa palavra, '{digite}', possui {contador} letras maiúsculas.")
print ("[format()] Essa palavra, '{}' possui {} letras maiúsculas.".format(digite, contador))

###############################QUESTÃO 8#####################################

produtos = {"arroz": 20, "feijão": 20, "bicicleta": 1400}

escolha = input("Digite um produto da lista: ")

def busca_preco(produtos, escolha):
    if escolha in produtos:
        return produtos[escolha]
    else:
        return "Produto", {escolha}, "não encontrado"
    

p1 = busca_preco(produtos, "Arroz")
p2 = busca_preco(produtos, "Feijão")
p3 = busca_preco(produtos, "bicicleta")


print(f"[f-string] O preço de Arroz é: {p1}")
print(f"[f-string] O preço de Feijão é: {p2}")
print(f"[f-string] O preço de Carne é: {p3}")


print("[format()] O preço de Arroz é: {}".format(p1))
print("[format()] O preço de Feijão é: {}".format(p2))
print("[format()] O preço de Carne é: {}".format(p3))

###############################QUESTÃO 9###############################################

def lista(numeros):
    soma = 0
    maior = menor = numeros[0]

    for n in numeros:
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    return soma, maior, menor

numeros = []

print("Digite 5 números inteiros:")
for i in range(5):
    num = int(input(f"{i+1}º número: "))
    numeros.append(num)

soma, maior, menor = lista(numeros)

print(f"\n[f-string] Soma: {soma}, Maior: {maior}, Menor: {menor}")
print("[format()] Soma: {}, Maior: {}, Menor: {}".format(soma, maior, menor))

#######################################QUESTÃO 10#########################################

opcao = ""
notas = (7.5, 8.0, 5.0, 9.0, 6.5)

soma = 0
for n in notas:
    soma += n
    media = soma / len(notas)

    if media >= 9:
       desempenho = "Excelente"
    elif media >= 7:
       desempenho = "Bom"
    elif media >= 5:
       desempenho = "Regular"
    else:
       desempenho = "Ruim"

    print(f"\n[f-string] Média: {media:.2f} | Desempenho: {desempenho}")

    print("[format()] Média: {:.2f} | Desempenho: {}".format(media, desempenho))

    opcao = input("\nDigite 'sair' para encerrar ou Enter para continuar: ")
print("Programa encerrado.")

###########################################QUESTÃO 11################################################

def resultado_alunos(alunos):
    resultados = {}
    for nome, nota in alunos.items():
        if nota >= 7:
            resultados[nome] = "Aprovado"
        else:
            resultados[nome] = "Reprovado"
    return resultados


alunos = {"Lucia": 4, "Hélder": 8, "Giovanna": 10}
resultado = resultado_alunos(alunos)

for nome, situacao in resultado.items():
  print(f"[f-string] {nome}: {situacao}")
print("[format()] {}: {}".format(nome, situacao))

########################################QUESTÃO 12####################################################

opcao = ''

while opcao.lower() != 'sair':
    palavra = input("\nDigite algo (ou 'sair' para encerrar):")
    if palavra.lower() == 'sair':
        break
    vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    contador = 0

    for letra in palavra.lower():
        if letra in vogais:
            contador +=1
    print (f"[f-string] A palavra '{palavra}' possui {contador} vogais.")
    print ("[format()] A palavra '{}' possui {} vogais. ".format(palavra, contador))
    #opcao = input("\nDigite 'sair' para encerrar ou Enter para continuar: ")
print('Programa encerrado.')

##########################################QUESTÃO 13###################################################

def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else "Divisão por zero não é permitida"
    return soma, subtracao, multiplicacao, divisao

n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número: "))

resultado = operacoes(n1, n2)

print(f"[f-string] Soma: {resultado[0]}, Subtração: {resultado[1]}, "f"Multiplicação: {resultado[2]}, Divisão: {resultado[3]}")
print("[format()] Soma: {}, Subtração: {}, Multiplicação: {}, Divisão: {}".format(resultado[0], resultado[1], resultado[2], resultado[3]))


#########################################QUESTÃO 14#######################################################

def coletar_nomes():
    nomes = []
    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        nomes.append(nome)
    return nomes

lista_nomes = coletar_nomes()

print(f"[f-string] Os nomes digitados foram: {lista_nomes}")
print("[format()] Os nomes digitados foram: {}".format(lista_nomes))

##################################################QUESTÃO 15#####################################################

def conta_maiusculas(texto):
    contador = 0
    for letra in texto:
        if letra.isupper():
            contador += 1
    return contador

frase = input("Digite um texto: ")
qtd = conta_maiusculas(frase)

print(f"[f-string] O texto '{frase}' possui {qtd} letras maiúsculas.")
print("[format()] O texto '{}' possui {} letras maiúsculas.".format(frase, qtd))
