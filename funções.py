def somar(N1,N2):
    resultado=N1+N2
    print(resultado)
def subtrair(N1,N2):
    resultado=N1-N2
    print(resultado)
def multiplicar(N1,N2):
    resultado=N1*N2
    print(resultado)
def dividir(N1,N2):
    resultado=N1/N2
    print(resultado)
def menu():
    print("1.somar\n2subtrair\n3.multiplicar\n4dividir")
    op=input("escolha um:")
    x=float(input("um valor:"))
    y=float(input("outro valor:"))
    if op=="1":
        somar(x,y)
    elif op=="2":
        subtrair(x,y)
    elif op=="3":
        multiplicar(x,y)
    else:
        dividir(x,y)
def main():
    menu()
if __name__=="__main__":
    main()