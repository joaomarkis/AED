"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
                Classe de Grafo Lista e funções de busca (dfs/bfs)

                       Copyright(c) 2018 João Victor Marques dos Santos
"""""
from GraphM import GrafoMatriz
import numpy as np
class GrafoLista:
    '''
    Inicia a classe GrafoLista gerando as listas de adjacências, com o parametro do iterável e se é ou não direcionado.
    Q2. Ideal para utilização em grafos esparsos, sendo proporcional ao número de vertices e arcos, se tornando mais economico para grafos esparsos.
    '''
    def __init__(self, grupo, direcionado=False):
        self.__typegraph = 1
        self.__V = []
        self.__weight = False
        for x in grupo:
            if len(grupo)>2:
                self.__weight = True
            if x[0] not in self.__V:
                self.__V.append(x[0])
            if x[1] not in self.__V:
                self.__V.append(x[1])
        self.__listaAdjacencias = [[] for i in range(len(self.__V))]
        self.__E = 0
        self.__direcionado = direcionado
        for i in grupo:
            self.inserirAresta(i)
    @property
    def weight(self):
        return self.__weight
    @property
    def typegraph(self):
        return self.__typegraph
    @property
    def V(self):
        return len(self.__V)
    #Retorna o número de arestas
    @property
    def E(self):
        return self.__E
    def inserirAresta(self, tuplex):
        '''
        Lê as tuplas do iterável passado e insere as arestas para conectar os vértices na lista de acordo se é direcionado ou não
        :param tuplex: tupla que contém os elementos
        '''
        self.__E += 1

        if len(tuplex) >2:
            if self.__direcionado:
                self.__listaAdjacencias[tuplex[0]].append((tuplex[1],tuplex[2]))
            else:
                self.__listaAdjacencias[tuplex[0]].append((tuplex[1],tuplex[2]))
                self.__listaAdjacencias[tuplex[1]].append((tuplex[0],tuplex[2]))
        else:
            if self.__direcionado:
                self.__listaAdjacencias[tuplex[0]].append(tuplex[1])
            else:
                self.__listaAdjacencias[tuplex[0]].append(tuplex[1])
                self.__listaAdjacencias[tuplex[1]].append(tuplex[0])
    @property
    def listaadj(self):
        return self.__listaAdjacencias
    def adj(self, x):
        return self.__listaAdjacencias[x]

    def transformGrafo(self):
        '''
        Transforma o grafo lista para o grafo matriz corretamente de acordo com o tipo de grafo que foi gerado.
        :return: retorna um GrafoMatriz igual ao GrafoLista
        '''
        aux =[]
        if self.__direcionado:
            for x in range(len(self.__listaAdjacencias)):
                for i in range(len(self.__listaAdjacencias)):
                    if self.__listaAdjacencias[x][i]>1:
                        aux.append((x,self.__listaAdjacencias[x][i][0], self.__listaAdjacencias[x][i][1]))
                    else:
                        aux.append((x,self.__listaAdjacencias[x][i]))
        else:
            aux2 = []
            for x in range(len(self.__listaAdjacencias)):
                aux2.append(x)
                for i in range(len(self.__listaAdjacencias[x])):
                    try:
                        if len(self.__listaAdjacencias[x][i]>1):
                            if self.__listaAdjacencias[x][i][0] in aux:
                                continue
                            else:
                                aux.append((x,self.__listaAdjacencias[x][i][0],self.__listaAdjacencias[x][i][1]))
                    except:
                        if self.__listaAdjacencias[x][i] in aux:
                            continue
                        else:
                            aux.append((x,self.__listaAdjacencias[x][i]))
        return GrafoMatriz(aux, self.__direcionado)

    def indegree(self, vertice):
        '''
         Método que analisa o grau de entrada do vértice passado como parametro, conta quantas arestas estão ''direcionadas'' para o vértice.
        :param vertice: vértice checado
        :return: retorna o grau do vértice
        '''
        count = 0
        try:
            if len(self.__listaAdjacencias[0][0])>1:
                for x in range(len(self.__listaAdjacencias)):
                    for i in range(len(self.__listaAdjacencias[x])):
                        if x == vertice:
                            break
                        elif vertice == self.__listaAdjacencias[x][i][0]:
                            count+=1
        except:
            for x in range(len(self.__listaAdjacencias)):
                if x == vertice:
                    continue
                elif vertice in self.__listaAdjacencias[x]:
                    count +=1
        return count
    '''
    Retorna a quantidade de arestas que o vértice passado está apontando, no caso seu grau de saída. 
    '''
    def outdegree(self, vert):
        return len(self.__listaAdjacencias[vert])


    def __str__(self):
        termo_str = ""
        for x in range(len(self.__listaAdjacencias)):
            termo_str +=str(x)+":"
            for i in range(len(self.__listaAdjacencias[x])):
                if i == len(self.__listaAdjacencias[x])-1:
                    termo_str+= "{}\n".format(self.__listaAdjacencias[x][i])
                else:
                    termo_str += "{}-->".format(self.__listaAdjacencias[x][i])
        return termo_str


    def __repr__(self):
        termo_str = "Grafo("
        if self.__direcionado:
            for x in range(len(self.__listaAdjacencias)):
                for i in range(len(self.__listaAdjacencias[x])):
                    print(self.__listaAdjacencias[x][i])
                    try:
                        if len(self.__listaAdjacencias[x][i])>1:
                            termo_str += "({},{},{}),".format(x, self.__listaAdjacencias[x][i][0],self.__listaAdjacencias[x][i][1])
                    except:
                            termo_str += "({},{}),".format(x, self.__listaAdjacencias[x][i])
            termo_str += " True)"
        else:
            aux = []
            for x in range(len(self.__listaAdjacencias)):
                aux.append(x)
                for i in range(len(self.__listaAdjacencias[x])):
                    try:
                        if len(self.__listaAdjacencias[x][i])>1:
                            if self.__listaAdjacencias[x][i][0] in aux:
                                continue
                            else:
                                termo_str +="({},{},{}),".format(x, self.__listaAdjacencias[x][i][0], self.__listaAdjacencias[x][i][1])
                    except:
                        if self.__listaAdjacencias[x][i] in aux:
                            continue
                        else:
                            termo_str += "({},{}),".format(x, self.__listaAdjacencias[x][i])
            termo_str= termo_str[0:-1]
            termo_str +=")"

        return termo_str
    def tree(self):
        aux = []
        if self.__E != len(self.__V)-1:
            return False
        else:
            for x in range(len(self.__listaAdjacencias)):
                grau = self.indegree(x)
                if grau == 2:
                    grau = self.outdegree(x)
                    if grau == 2:
                        aux.append(x)
            if len(aux) == len(self.__listaAdjacencias):
                return False
            else:
                return True