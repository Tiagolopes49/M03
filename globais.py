nome="Joaquim"
resultado=0
x=0
y=0

def cumprimentarv3():
    print(f"Bom Dia {nome}")

def somar():
    global resultado,x,y
    resultado=x+y
    x=0
def main():
    global x,y
    #cumprimentarv3()
    x=10
    y=5
    somar()
    print(resultado)
if __name__=="__main__":
    main()