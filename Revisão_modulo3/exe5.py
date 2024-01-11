#Tiago Lopes Nº28 10ºT
#o programa calcula o signo de cada pessoa
def calcula_signo(dia,mes):
    if (mes==6 and dia>21) or (mes==7 and dia<22):
        print("o teu signo é cancer")
    else:
        print("data inválida")

#programa principal
mes=int(input("Introduza o seu mês: "))
dia=int(input("Introduza o dia um que nasceu: "))
calcula_signo(dia,mes)