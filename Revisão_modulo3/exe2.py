#Tiago Lopes nº28 10ºT
#o programa converte uma quantidade de tempo em minutos
def converter_para_segundos(minutos):
    segundos=minutos*60
    return segundos

minutos=int(input("Introduza os minutos: "))
print(converter_para_segundos(minutos))