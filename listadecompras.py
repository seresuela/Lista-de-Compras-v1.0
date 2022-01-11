# -*- coding: utf-8 -*-

"""
Lista de Compras v1.0
Lançamento: 11 de Janeiro de 2022
Autora: Stephani Seresuela
Função: Listar as compras necessárias
"""

print("----- ♥ LISTA DE COMPRAS ♥ -----")

lista = []

editar = False

editar = input("Deseja editar a lista? (s/n): ")
while editar == "s":
	lista.append(input("Item: "))


	add = input("Deseja adicionar mais itens? (n/s)")
	if add == "n":
		print("--- Lista: ---")
		for i in lista:
 			print("•" + " " + i)
		print("--- Boas compras! ---")
		editar = True






