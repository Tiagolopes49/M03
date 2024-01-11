#Tiago Lopes Nº28 10ºT
#o programa calcula o custo total de uma corrida de taxi
def custo_total_taxi(km):
    base=4
    return base+km*0.5

km=float(input("Introduza os km percorridos: "))
print(custo_total_taxi(km))
