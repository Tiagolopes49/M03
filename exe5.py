def primo(numero):
    for i in range(2,numero):
        resto=numero%i
        if resto==0:
            print("não é primo")
            return
    print("é primo")
primo(10)
primo(7)