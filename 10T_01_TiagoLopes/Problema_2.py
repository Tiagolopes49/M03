#Tiago Lopes Nº28 10ºT
#o programa determina o sigono a que uma pessoas pertence
def signo(dia,mes):
    if (mes==1 and dia>=21) or (mes==2 and dia<=19):
        print(" O teu signo é Aquario")
    elif (mes==2 and dia>=20) or (mes==3 and dia<=20):
        print(" O teu signo é Peixes")
    elif (mes==3 and dia>=21) or (mes==4 and dia<=20):
        print(" O teu signo é Áries")
    elif (mes==4 and dia>=21) or (mes==5 and dia<=20):
        print(" O teu signo é Touro")
    elif (mes==5 and dia>=21) or (mes==6 and dia<=20):
        print(" O teu signo é Gémeos")
    elif (mes==6 and dia>=21) or (mes==7 and dia<=21):
        print(" O teu signo é Câncer")
    elif (mes==7 and dia>=22) or (mes==8 and dia<=22):
        print(" O teu signo é Leão")
    elif (mes==8 and dia>=23) or (mes==9 and dia<=22):
        print(" O teu signo é Virgem")
    elif (mes==9 and dia>=23) or (mes==10 and dia<=22):
        print(" O teu signo é Libra")
    elif (mes==10 and dia>=23) or (mes==11 and dia<=21):
        print(" O teu signo é Escorpião")
    elif (mes==11 and dia>=22) or (mes==12 and dia<=21):
        print(" O teu signo é Sagitário")
    elif (mes==12 and dia>=22) or (mes==1 and dia<=20):
        print("O teu signo é Capricórnio")
    else:
        print("Data incorreta")
#programa principal
dia=int(input("Introduza o dia :"))
mes=int(input("Introduza o mês: "))
print(signo(dia,mes))