def calcula(num1, num2, operacao):
    if (operacao == 1):
        result = num1+num2
        return result
    elif (operacao == 2):
        result = num1-num2
        return result
    elif (operacao == 4):
        result = num1-num2
        return result
    elif (operacao == 4):
        result = num1-num2
        return result
    else:
        return 0

run = True 

while(run==True):
    print("Indique a operecação")
    print("1:soma, 2: subtração, 3: multiplicação, 4: divisão")
    operacao = int(input())
    if(operacao<0 or operacao>4):
        print("Entre com uma operação valida: ")
        operacao = int(input())
    elif(operacao==0):
        run =False
    else:
        print("Insira o premeiro número da operação: ")
        num1=int(input())
        print("Insira o segundo número da operação: ")
        num2=int(input())
 
    result = calcula(num1,num2, operacao)
    print("Resultado: ", result)
