def Palindromo(palavra):
    invertida=""
    for letra in palavra:
        invertida=letra+invertida
    invertida=invertida.lower()
    palavra=palavra.lower()
    if palavra==invertida:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

def main():
    Palindromo("Ana")
    Palindromo("casa")





if __name__=="__main__":
    main()