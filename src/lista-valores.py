lista = [20, 9, 8, 7]

resposta_par = 0
resposta_impar = 1

for num in lista:
    if num % 2 == 0:
        resposta_par = resposta_par + num
    else:
        resposta_impar = resposta_impar * num

    
print(f"\nA soma dos valores pares é: {resposta_par} \nA multiplicação dos valores impares é: {resposta_impar}")