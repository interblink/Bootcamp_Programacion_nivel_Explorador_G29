# -*- coding: utf-8 -*-
numero = int(input())
triangular = 0
nivel = 0

while triangular < numero:
    nivel += 1
    triangular = (nivel * (nivel + 1)) // 2

if triangular == numero:
    print(f"{numero} es adecuado para apilar.")
else:
    print(f"{numero} no es adecuado para apilar.")