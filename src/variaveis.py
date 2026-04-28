### Váriaveis do tipo string (str) texto

print("\nVáriaveis do tipo string (str) texto:")

nome = "Poliana"
sobrenome = "Oliveira"

print(f"Seu nome completo é: {nome} {sobrenome}")
print("O tipo da variável nome é: " + str(type(nome)))
print("O tipo da variável sobrenome é: " +str(type(sobrenome)))


### Váriaveis do tipo integer (int) 

print("\nVáriaveis do tipo integer (int):")

idade_carla =  18
idade_poli = 29

idade_irmas = idade_carla + idade_poli

print (f"A soma das idades das irmãs é: {idade_irmas}")
print("O tipo da variável idade_carla é: " + str(type(idade_carla)))
print("O tipo da variável idade_poli é: " +str(type(idade_poli)))
print("O tipo da variável idade_irmas é: " +str(type(idade_irmas)))

### Váriaveis do tipo float (float) números decimais:

print("\nVariáveis do tipo float (float) números decimais:")

altura = 1.80
peso = 97.5

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.3f}")
print("O tipo da variável altura é: " + str(type(altura))) 
print("O tipo da variável peso é: " + str(type(peso))) 
print("O tipo da variável imc é: " + str(type(imc)))

### ========== Variáveis do tipo boolean (bool) verdadeiro ou falso ==========
print("\nVariáveis do tipo boolean (bool) verdadeiro ou falso:")

casado = True

if casado:
    print("Você é casado.")
else:    
    print("Você não é casado.")

print(f"Seu casamento é: {casado}")
print("O tipo da variável casado é: " + str(type(casado)))