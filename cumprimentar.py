def cumprimentar():
    print("Bom Dia")
def cumprimentarv2():
    nome=input("Qual o seu nome?")
    print(f"Bom Dia {nome}")
def cumprimentarv3(nome):
    print(f"Bom Dia {nome}")
    nome=""
def main():
    nome=input("Qual o seu nome")
    cumprimentarv3(nome)
    print(nome)
if __name__=="__main__":
    main()
