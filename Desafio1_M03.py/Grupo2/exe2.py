def MaiorOuMenor(x1,x2,x3):
    #maior
    if x1>=x2 and x1>=x3:
        maior=x1
    elif x2>=x3:
        maior=x2      
    else:
        maior=x3
    #menor
    if x1<=x2 and x1<=x3:
        menor=x1
    elif x2<=x3:
        menor=x2      
    else:
        menor=x3
    if x1>0 and x2>0 and x3>0:
        return maior
    elif x1<0 and x2<0 and x3<0:
        return menor
    else:
        return None