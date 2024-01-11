#Tiago Lopes Nº28 10ºT
#o programa que calcula 125 segundos
#//Divisão é usada para encontar o nº inteiro
#%resto da divisão é usada para encontrar os segundos
def converter_para_minutos(segundos):
    minutos=segundos//60
    segundos_restantes=segundos%60
    return minutos, segundos_restantes

segundos=int(input("Introduza os segundos: "))
print(converter_para_minutos(segundos))
minutos,segundos_restantes=converter_para_minutos(segundos)
print(f"{segundos}segundos são {minutos} minutos e {segundos_restantes}segundos")