# -*- coding: utf-8 -*-
"""Exercicio Calculadora

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CE5BpcTnm_rnfpHXb6oY31sAnrkH1jJe
"""

'''
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
'''

def calcula(valor1, valor2, operacao):
  if operacao == 1: return valor1 + valor2
  elif operacao == 2: return valor1 - valor2
  elif operacao == 3: return valor1 * valor2
  elif operacao == 4: return valor1 / valor2
  else: return 0

valor1 = float(input("Insira valor 1: "))
valor2 = float(input("Insira valor 2: "))
operacao = int(input(f"Insira operação sendo \n1 = soma \n2 = subtração \n3 = multiplicação \n4 = divisão \n"))

resultado = calcula(valor1, valor2, operacao)
print(f"O resultado da operação escolhida é ",resultado)

