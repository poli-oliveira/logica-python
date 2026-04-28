print ("\nVelocidade máxima permitida e verificação de CNH válida")

velocidade_max = int(input("\nEm qual velocidade o veiculo se encontrava? "))
cnh_valida = input("O motorista possui CNH válida? (sim/não) ")

valido = cnh_valida == "sim"
if valido:
    if velocidade_max <= 80:
        print ("A CNH do condutor está válida e veiculo estava dentro da velocidade permitida!")
    elif velocidade_max > 80 and velocidade_max <= 90:
        print (f"A CNH do condutor está válida. Mas o veiculo estava a {velocidade_max}km/h, a velocidade permitida é de 80km/h: MULTA LEVE!")
    elif velocidade_max > 90 and velocidade_max <= 100:
        print (f"A CNH do condutor está válida. Mas o veiculo estava a {velocidade_max}km/h, a velocidade permitida é de 80km/h: MULTA GRAVE!")
    else:
        print (f"A CNH do condutor está válida. Mas o veiculo estava a {velocidade_max}km/h, a velocidade permitida é de 80km/h: MULTA GRAVÍSSIMA!")    
else:
    if velocidade_max <= 80:
        print ("O veiculo estava dentro da velocidade permitida, no entanto a CNH está inválida: MULTA GRAVÍSSIMA!")
    else:
        print (f"A CNH do condutor está invalida e o veiculo estava a {velocidade_max}km/h, a velocidade permitida é de 80km/h: MULTA GRAVÍSSIMA!")
    
