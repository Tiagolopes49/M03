#Tiago Lopes Nº28 10ºT
#o programa conta os digitos de um numero
def contar_digitos(n):
    n=str(n)       #transforma um nº numa string
    print(len(n))  #o len dá o comprimento de uma string
    
n=int(input("introduza um numero: "))
contar_digitos(n)