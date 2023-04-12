# REVISÃO PARA A AVALIAÇÃO DO DIA 19.04.2023

def exibir_nome():
    print("Mark")

# ------------------------------------------

def soma_2_num(a: int, b: int):
    soma = a + b
    return soma

# ------------------------------------------

print(soma_2_num(37,90))

# ------------------------------------------

# ATIVIDADE:

# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere 'P', se seu argumento for positivo;
# e 'N' se seu argumento for zero ou negativo.


def argumento(n: int ):
    if n> 0:
        print("P")
    else:
        print("N")

argumento(int(input("Digite um número: ")))