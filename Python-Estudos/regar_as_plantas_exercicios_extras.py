# -*- coding: utf-8 -*-
"""Regar as plantas - Exercicios Extras

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZuEE2q4WDRTlhNR42Q0gkn_gRWhhsP2w
"""

# Regar as batatas agora elas estão em outra ordem
# 0-tomate, 1-tomate, 2-tomate, 3-batata, 4-batata, 5-batata

for i in range(6):
  if i not in (0,1,2):
    planta = i
    print("Regue a planta", planta)

# Regar somente as batatas (outra forma)
plantas = ["Batatas"]
for item in plantas:
    print(item)

# Regar somente o tomate agora elas estão em outra ordem
# 0-tomate, 1-tomate, 2-batata, 3-batata, 4-tomate, 5-tomate
# if i not in (2,3):

for i in range(6):  
  if i != 2 or 3:
    planta = i
    print("Regue a planta", planta)

# Regar somente as tomates (outra forma)
plantas = ["Tomates"]
for item in plantas:
    print(item)

# Regar todas mas agora de trás para frente
# 0-tomate, 1-batata, 2-cenoura, 3-tomate, 4-batata, 5-cenoura

for i in range(5,-1,-1):
  #if i not in (2,3):
  planta = i
  print("Regue a planta", planta)

# Regando as plantas de trás p/ frente (outra forma usando reverse)
plantas = ["Tomate 0","Batata 1","Cenoura 2","Tomate 3","Batata 4","Cenoura 5"]
plantas.reverse()
print(plantas)