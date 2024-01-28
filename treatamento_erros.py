print("digite seu nome: ")
nome = input()

executar = 1

while(executar==1):
    print("Entre com o ano de nascimento: ")
    try:
        ano = int(input())
        if (ano < 1924) or (ano > 2024):
            print("Intervalo entre 1993 e 2024")
        else:
            idade = 2024 - ano
            print("O usuaários ",nome,"completará", idade, "anos em 2024" )
            executar = 0
    except:
        print("Os anos devem ser digitados em números")
