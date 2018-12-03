"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
                

                       Copyright(c) 2018 João Victor Marques dos Santos
"""""
import numpy as np
import sys

class Locomotive_Profit:
    '''
    Classe que trabalha as informações passadas por um .txt e retorna o valor máximo possível dos itens carregados
    de acordo com seu limite de peso suportado e retorna os itens utilizados para chegar nesta solução.
    '''
    def __init__(self):
        self.weight = []
        self.values = []
        self.weightMax = 0
        self.n = 0
        self.__run_Text()
        self.memorie_values = np.array([[0] for i in range((self.n + 1) * (self.weightMax + 1))]).reshape(self.n + 1, self.weightMax + 1)
        self.__run_Profit_Count()

    def __run_Profit_Count(self):
        max_profit = self.great_profit()
        item_profit = self.return_item()
        print("Valor de lucro máximo é:",max_profit)
        print("Os itens escolhidos são:",item_profit)
    def __run_Text(self):
        text = open(str(sys.argv[1]),"r")
        text = text.read()
        text = text.replace(",","\n")
        text = text.split()
        self.weightMax = int(text[0])#O primeiro elemento é o peso total que a locomotiva suporta
        boolean = True
        for element in range(1,len(text)):#Range a partir de 1 já que o primeiro elemento é o peso total suportado
            if boolean:
                self.weight.append(int(text[element]))#Nesta ordem, o primeiro elemento sempre é o peso o segundo o valor
                boolean = False#Boolean False para o próximo elemento ser adicionado na lista de valores
            else:
                self.values.append(int(text[element]))
                boolean = True
        self.n = len(self.weight)
    def great_profit(self):
            "Função que retorna o maior lucro possível com o limite de peso da locomotiva"
            if self.weightMax == 0 or self.values == 0:#Se o peso suportado da locomotiva é 0, então o lucro é 0
                return 0
            for i in range(1,self.n+1):#Range a partir de 1 já que a linha 0 da tabela é apenas de valores 0
                for p in range(1, self.weightMax + 1):
                    if self.weight[i - 1] <= p:#Caso o peso do objeto seja menor que o peso suportado
                        self.memorie_values[i, p] = max((self.memorie_values[i - 1, p - self.weight[i - 1]] + self.values[i - 1]), self.memorie_values[i - 1, p])#A posição atual decide se vale a pena colocar o objeto dentro da mochila ou recuperar o valor ótimo da solução da linha anterior
                    else:
                        self.memorie_values[i, p] = self.memorie_values[i - 1, p]#A tabela preenche esta posição com o valor da solução ótima já descoberta na linha anterior

            return (self.memorie_values[self.n, self.weightMax])#Retorna o valor de lucro máximo

    def return_item(self):
        aux = self.weightMax
        "Função que descobre todos os itens que foram utilizados para preencher a locomotiva com seu lucro máximo"
        item_list = []
        for i in range(self.n,0,-1):#Percorre a tabela do fim para inicializar com a posição de lucro máximo
            if not self.memorie_values[i, aux] == self.memorie_values[i - 1, aux]:#Verifica se o valor da linha anterior é igual, caso não seja, significa que este item foi adicionado na locomotiva
                item_list.append(i)#Adiciona o item na lista
                aux -= self.weight[i - 1]#Retira o peso do item do peso total pesquisado para descobrir o próximo item que tenha sido colocado
        return item_list#Retorna lista de itens
if __name__ == "__main__":
    x = Locomotive_Profit()

