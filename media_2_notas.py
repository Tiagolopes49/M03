#Tiago Lopes Nº28 10ºT
#o programa calcula a media de 3 notas e mostra um nome
def media_tres_notas(nota1,nota2,nota3):
    media=(nota1+nota2+nota3)/3
    print(media)

def nome_aluno(n):
    print(n)

#programa principal
nota1=float(input("introduza a primeira nota"))
nota2=float(input("introdduza a segunda nota"))
nota3=float(input("introduza a terceira nota"))
n=input("introduza um nome: ")

media_tres_notas(nota1,nota2,nota3)
nome_aluno(n)