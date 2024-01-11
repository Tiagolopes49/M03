#Tiago Lopes Nº28 10ºT
#o programa converte uma quantidade de tempo em segundos
def converter_para_minutos(segundos):
    minutos=(segundos*1)/60
    return minutos

segundos=int(input("Introduza os segundos: "))
print(converter_para_minutos(segundos))