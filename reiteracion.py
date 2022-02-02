#Algoritmo para calcular factoria utilizando reiteracion

def factor (n) :
    if n==0 or n==1 :
        resultado = 1
        
    elif n > 1:
        resultado = n * factor (n-1)
        
    return resultado

f=factor(5)
print(f)
