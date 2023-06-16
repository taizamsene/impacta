import os
 
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
 
print("Seu IMC é: %.4f" % imc)

if imc < 18.5:
	print("Magreza")
elif imc < 24.9:
	print("Normal")
elif imc < 30:
	print("Sobrepeso")
elif imc > 30:
	print("Obesidade")
    
os.system("pause")
