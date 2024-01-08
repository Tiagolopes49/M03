#Tiago Lopes Nº28 10ºT
#programa que mostra os numeros de 1 a 5 na forma crescente e decrescente
def crescente(n):
    for i in range(1,n+1,1):
        print(i)

def decrescente(n):
    for i in range(n,0,-1):
        print(i)

#programa principal
crescente(5)
print()
decrescente(5)