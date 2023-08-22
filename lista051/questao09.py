'''
9) Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2.
'''

cont = 2
acumulador = 0
while (cont <= 500):
    print(cont)
    acumulador = acumulador + cont
    cont = cont + 2

print(f"A soma de todos os valores pares é {acumulador}")