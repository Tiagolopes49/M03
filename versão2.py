def somar(N1,N2):
    resultado=N1+N2
    return resultado
def subtrair(N1,N2):
    resultado=N1-N2
    return resultado
def multiplicar(N1,N2):
    resultado=N1*N2
    return resultado
def dividir(N1,N2):
    resultado=N1/N2
    return resultado
def menu():
    while True:
        print("1.somar\n2subtrair\n3.multiplicar\n4dividir\n5sair")
        op=input("escolha um:")
        if op=="5":
            break
        x=float(input("um valor:"))
        y=float(input("outro valor:"))
        if op=="1":
            R=somar(x,y)
        elif op=="2":
            R=subtrair(x,y)
        elif op=="3":
            R=multiplicar(x,y)
        else:
            R=dividir(x,y)    
        print(R)
def main():
    menu()
if __name__=="__main__":
    main()