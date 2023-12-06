alfabeto="abcdefghijklmnopqrstuvwxyz"
codigo="bcdefghijklmnopqrstuvwxyza"
def Codifica(texto):
    global alfabeto, codigo
    codificado=""
    texto=texto.lower()
    for letra in texto:
        if letra in alfabeto:
            posicao=alfabeto.index(letra)
            codificado=codificado+codigo[posicao]
        else:codificado=codificado+letra
    return codificado

def Descodifica(texto):
    global alfabeto, codigo
    descodificado=""
    texto=texto.lower()
    for letra in texto:
        if letra in codigo:
            posicao=codigo.index(letra)
            descodificado=descodificado+alfabeto[posicao]
        else:
            descodificado=deacodificado+letra
    return descodificado

print(Codifica("bebe"))
print(Codifica("cfcf"))