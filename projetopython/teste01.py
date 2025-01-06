print("Olá mundo, testando python.")

#variáveis e tipos básicos
nome = "maria"
idade = 27
altura = 1.68
esta_estudando = True
print(nome,idade,altura, esta_estudando)

nome = input("Digite seu nome: ")
print("Olá,",nome,"seja bem-vindo!")

#soma de dois numeros
num1 = float(input("Digite o primeiro nº: "))
num2 = float(input("Digite o segundo nº: "))
print("A soma é:", num1 + num2)

num = int(input("Digite um nº: "))
if num % 2 ==0:
    print("O número é par.")
else:
    print("O número é impar.")