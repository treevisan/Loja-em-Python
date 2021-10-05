import sys

def obter_limite():
    global idade
    nome = ("Olá, eu me chamo Gabrieli Trevisan! \nSeja bem vindo a minha loja, Produtos Biodegradáveis.")
    print (nome)
    cargo = str(input('Farei uma análise de crédito para você. Para isso preciso que digite o cargo que exerce na empresa em que trabalha atualmente: '))
    salario = float(input("Informe seu salário atual: "))
    if salario <= 0:
        print('Salário inválido.')
        sys.exit()
    else:
        ano = int(input('Informe seu ano de nascimento: '))
        if ano >= 2021:
            print('Ano de nascimento inválido.')
            sys.exit()
        else:
            print(f'Seu cargo atual é: {cargo} \nSeu salário atualmente é: {salario}  \nSeu ano de nascimento é: {ano}')
            idade = 2021 - ano
            print(f'Sua idade é aproximadamente {idade} anos')
            limite = salario * (idade / 1000) + 100
    return limite


def verificar_produto(limite):
    global idade
    print("")
    produto = str(input('Digite o nome do produto em que deseja adquirir: '))
    preco_produto = float(input('Digite o preço do produto em que deseja: '))
    if preco_produto <= 0:
        print('Valor inválido.')
        sys.exit()
    else:
        nome_completo = ('Gabrieli Trevisan')
        quantidade_caracteres_completo = len(nome_completo)
        primeiro_nome = (nome_completo.split()[0])
        caracteres_primeiro_nome = len(primeiro_nome)
        desconto = 0
        bloqueado = False

        if preco_produto <= (0.6 * limite):
            print('Liberado.')
        elif preco_produto < (0.9 * limite):
            print('Liberado ao parcelar em até 2 vezes.')
        elif preco_produto <=  limite:
            print('Liberado ao parcelar em 3 ou mais vezes.')
        else:
            print('Bloqueado.')
            bloqueado = True

        if (not bloqueado):
            if (quantidade_caracteres_completo<preco_produto<idade):
                desconto = caracteres_primeiro_nome
                print(f"Você terá um desconto de: {desconto} reais")
                preco_produto -= desconto
                print('Valor com desconto: %.2f' %preco_produto)
            else:
                print('Não haverá descontos.')
            limite -= preco_produto
    return limite

#Programa Principal
preco_produto = 0
idade = 0
limite = obter_limite()
print('O valor limite de gasto que você pode utilizar na loja é: %.2f'%limite)
quantidade_produtos = int(input('Informe quantos produtos deseja cadastrar: '))

c = 1
if quantidade_produtos <= 0:
    print('Quantidade de produtos inválido.')
    sys.exit()
else:
    while c <= quantidade_produtos:
        if limite <= 0:
            print('Limite indisponível.')
            break
        else:
            limite = verificar_produto(limite)
            c += 1
            print('Seu limite agora é: %.2f'%limite)
print('Fim.')

