def Media():
    soma=0
    for i in range(5):
        n=int(input("Valor:"))
        #somar o valor
        soma=soma+n
    media=soma/5
    pritn(media)