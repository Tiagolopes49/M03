import sys

def Vogais(palavra):
    contar=0
    Vogais="a,e,i,o,u,A,E,I,O,U"
    for letra in palavra:
        if letra in Vogais:
            contar=contar+1
    print(contar)

def main():
    if len (sys.argv)!=2:
        palavra=input("Introduza uma palavra")
    else:
        palavra=sys.argv[1]
    Vogais(palavra)    
if __name__=="__main__":
    main()