def calcula(numA, numb, operacao):
    if(operacao==1):
        return numA+numb    
    elif (operacao==2):
        return numA-numb
    elif (operacao==3):
        return numA*numb
    elif (operacao==4):
        return numA/numb
    else:
        return 0
result = calcula(1,2,3)
print(result) 
