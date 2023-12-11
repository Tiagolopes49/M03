import random
def CPU_Joga():
    opcao=random.randint(1,3)
    if opcao==1:
        return "pedra"
    elif opcao==2:
        return "papel"
    else:
        return "tesoura"

def Player_Joga():
    while True:    
        escolha=input("escolha pedra, papel ou tesoura")
        if escolha in ("tesoura","papel","pedra"):
            break
    return escolha

def Vitoria(p1,p2):
    if p1=="pedra" and p2=="tesoura":
        return True
    if p1=="tesoura" and p2=="papel":
        return True
    if p1=="papel" and p2=="pedra":
        return True
    return False

def Testar_Vitoria(jogada_pc, jogada_player):
    print(f"Computador: {jogada_pc}")
    print(f"Player: {jogada_player}")
    if Vitoria(jogada_pc,jogada_player)==True:
        print("Computador ganha!")
        return True
    if Vitoria(jogada_player,jogada_pc)==True:
        print("Player ganha")
        return True
    return False
    
def main():
    while True:
        jogada_cpu=CPU_Joga()
        jogada_player=Player_Joga()
        alguem_ganhou=Testar_Vitoria(jogada_cpu,jogada_player)
        if alguem_ganhou==True:
            break
        else:
            print("Empate!")

if __name__=="__main__":
    main()