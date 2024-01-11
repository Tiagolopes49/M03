#Tiago Lopes Nº28 10ºT
#o programa que calcula o montante total a ser pago por um empréstimo
def calcular_juros(juros,anos):
    montante_final=montante_inicial*(1+taxa_de_juros/100)**numero_anos
    print(f"{montante_final:.2f}")
montante_inicial=int(input("Introduza montante incial: "))
taxa_de_juros=int(input("Introduza a taxa de juros: "))
numero_anos=int(input("Introduza o numero de anos: "))
calcular_juros(taxa_de_juros,numero_anos)