numero=5
def tabuada():
    global numero
    for i in range(1,11):
        M=i*numero
        print(f"{i}*{numero}={M}")
    numero=0
tabuada()