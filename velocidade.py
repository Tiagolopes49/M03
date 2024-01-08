#Tiago Lopes Nº28 10ºT
#o programa que queria um menu que calcula a velocidade
def mostrar_formula():
    print("V=V0+a*t")

def calcular_velocidade():
    V=V0+a*t
    return V
opcao = -1
while opcao != 0:
    print("Escolha a opção: ")
    print()
    print("1-mostra formula")
    print("2-calcular velocidade")
    print("0-Sair")
    print()
    opcao = int(input("Digite a operação a realizar: "))
    if (opcao == 1):
        mostrar_formula()
    elif (opcao == 2):
        V0=float(input("introduza a velocidade inicial"))
        a=float(input("introduza a acelaração"))
        t=float(input("introduza o tempo"))
        print(calcular_velocidade())
    elif (opcao!=0):
        print("Não é uma opção válida!")
    print()
print("Programa terminou!")