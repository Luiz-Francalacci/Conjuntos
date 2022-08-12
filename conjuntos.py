# -*- coding: utf-8 -*-
arquivo = open('teste1.txt', 'r')  #abertura de arquivo e definindo contador
leitura = arquivo.readlines()
txtModificado = []
for linha in leitura:
    if linha[-1] == "\n":
        txtModificado.append(linha[: -1])
    else:
        txtModificado.append(linha)

numeroOperacoes = int(txtModificado[0])

def uniao(array1, array2):       #funcão de uniao
    arr1 = array1
    arr2 = array2
    arrf = []
    for i in arr1:
        arrf.append(i)
    for j in arr2:
        arrf.append(j)
    arrf.sort()
    return arrf


def intersecao(array1, array2):     #funcão de intersecao
    arr1 = array1
    arr2 = array2
    arrf = []
    for i in arr1:
        for j in arr2:
            if i == j:
                arrf.append(i)
    arrf.sort()
    return arrf

def diferenca(array1, array2):    #funcão de diferença
    arr1 = array1
    arr2 = array2
    arrf = []
    for i in arr1:
        if i not in arr2:
            arrf.append(i)
    for j in arr2:
        if j not in arr1:
            arrf.append(j)
    arrf.sort()
    return arrf

def cartesiano(array1, array2):     #funcão produto cartesiano
    arr1 = array1
    arr2 = array2
    pc = [(x,y) for x in arr1 for y in arr2]
    return pc


while numeroOperacoes != 0:                      #Loop de funcionamento
    for i in txtModificado:
        if i == "U":
            index = txtModificado.index(i)
            conjunto1 = txtModificado[index + 1]         #seção Uniao
            conjunto2 = txtModificado[index + 2]
            cc1 = conjunto1.split(', ')
            cc2 = conjunto2.split(', ')
            resposta = uniao(cc1, cc2)
            print("Uniao: conjunto 1: ", cc1, "conjunto 2: ", cc2, "Resultado: ", resposta)
            numeroOperacoes -= 1
            

        if i == "I":
            index = txtModificado.index(i)
            conjunto1 = txtModificado[index + 1]       #seção Intersecao
            conjunto2 = txtModificado[index + 2]
            cc1 = conjunto1.split(', ')
            cc2 = conjunto2.split(', ')
            resposta = intersecao(cc1, cc2)
            print("Intersecao: conjunto 1: ", cc1, "conjunto 2: ", cc2, "Resultado: ", resposta)
            numeroOperacoes -= 1
            

        if i == "D":
            index = txtModificado.index(i)
            conjunto1 = txtModificado[index + 1]      #seção Diferenca
            conjunto2 = txtModificado[index + 2]
            cc1 = conjunto1.split(', ')
            cc2 = conjunto2.split(', ')
            resposta = diferenca(cc1, cc2)
            print("Diferenca: conjunto 1: ", cc1, "conjunto 2: ", cc2, "Resultado: ", resposta)
            numeroOperacoes -= 1
            

        if i == "C":
            index = txtModificado.index(i)
            conjunto1 = txtModificado[index + 1]      #seção Produto Cartesiano
            conjunto2 = txtModificado[index + 2]
            cc1 = conjunto1.split(', ')
            cc2 = conjunto2.split(', ')
            resposta = cartesiano(cc1, cc2)
            print("Produto Cartesiano: conjunto 1: ", cc1, "conjunto 2: ", cc2, "Resultado: ", resposta)
            numeroOperacoes -= 1
            
            
            
    