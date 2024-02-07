#Tiago Lopes Nº28 10ºT
#o programa faz a conversão de segundos para minutos
def converter_para_minutos(segundos):
    minutos=segundos*1/60
    return minutos
#programa principal
segundos=int(input("Tempo obtido na prova(em segundos): "))
print(converter_para_minutos(segundos))