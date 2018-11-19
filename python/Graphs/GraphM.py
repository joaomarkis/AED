"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
                Classe de Grafo Matriz e funções de busca (dfs/bfs)

                       Copyright(c) 2018 João Victor Marques dos Santos
"""""

from GraphL import GrafoLista
import numpy as np
class GrafoMatriz:
    '''
    Inicia o GrafoMatriz com o iterável passado como parametro.
    Q2. O GrafoMatriz é ideal para ser utilizado em grafos densos, pois o número de arcos é similar ao espaço ocupado (V²).
        Requer apenas um bit por entrada, e é válido para outros tipos de Grafos, exemp: grafos ponderados.
    '''
    def __init__(self, grupo, direcionado=False):
        self.__V = []
        self.__typegraph = 0
        for x in grupo:
            if x[0] not in self.__V:
                self.__V.append(x[0])
            if x[1] not in self.__V:
                self.__V.append(x[1])
        self.__matrizAdjacencias = np.arange(len(self.__V), dtype=object)
        for x in range(len(self.__matrizAdjacencias)):
            self.__matrizAdjacencias = np.array([0]*len(self.__V)*len(self.__V)).reshape(len(self.__V),len(self.__V))
        self.__E = 0
        self.__direcionado = direcionado
        for i in grupo:
            self.inserirAresta(i)
    @property
    def matriz(self):
        return self.__matrizAdjacencias
    #Retorna o número de vertices
    @property
    def V(self):
        return len(self.__V)
    #Retorna o tipo do grafo
    @property
    def typegraph(self):
        return self.__typegraph
    #Retorna o número de arestas
    @property
    def E(self):
        return self.__E
    def inserirAresta(self, tuplex):
        '''
        Insere as arestas nos vértices passados pela tupla de elementos (com ou sem peso) e se é ou não direcionado.
        :param tuplex: tupla de elementos
        '''
        self.__E += 1
        if len(tuplex) >2:
            if self.__direcionado:
                self.__matrizAdjacencias[tuplex[0]][tuplex[1]] =(tuplex[2])
            else:
                self.__matrizAdjacencias[tuplex[0]][tuplex[1]] =(tuplex[2])
                self.__matrizAdjacencias[tuplex[1]][tuplex[0]] =(tuplex[2])
        else:
            if self.__direcionado:
                self.__matrizAdjacencias[tuplex[0]][tuplex[1]]= 1
            else:
                self.__matrizAdjacencias[tuplex[0]][tuplex[1]]=1
                self.__matrizAdjacencias[tuplex[1]][tuplex[0]]=1
    def transformGrafo(self):
        '''
        Transforma o GrafoMatriz para um GrafoLista corretamente
        :return: retorna um GrafoLista igual ao GrafoMatriz
        '''
        aux = []
        matriz_copia = np.array(self.__matrizAdjacencias)
        for x in range(len(matriz_copia)):
            for y in range(len(matriz_copia)):
                if int(matriz_copia[x][y]) == 1:
                    if int(matriz_copia[y][x]) == 1:
                        aux.append((x,y))
                        matriz_copia[x][y] = 0
                        matriz_copia[y][x] = 0
                    else:
                        aux.append((x,y))
                        matriz_copia[x][y] = 0
                elif int(matriz_copia[x][y]) >1:
                    if int(matriz_copia[y][x]) >1:
                        aux.append((x,y, matriz_copia[x][y]))
                        matriz_copia[x][y] = 0
                        matriz_copia[y][x] = 0
                    else:
                        aux.append((x,y, matriz_copia[x][y]))
                        matriz_copia[x][y] = 0
                else:
                    pass
        del matriz_copia
        aux = tuple(aux)
        return GrafoLista(aux, self.__direcionado)
    def indegree(self, vert):
        '''
        Conta qual seria o grau de entrada do vértice passado como parametro
        :param vert: vértice a ser contado o grau
        :return: o número referente ao grau do vértice
        '''
        count = 0
        for x in range(len(self.__matrizAdjacencias)):
            if x == vert:
                continue
            else:
                if self.__matrizAdjacencias[x][vert]>0:
                    count+=1
        return count
    def outdegree(self, vert):
        '''
        Conta o número do grau de saída do vértice passado como parametro
        :param vert: vértice a ser contado
        :return: o número referente ao grau do vértice
        '''
        count = 0
        for x in range(len(self.__matrizAdjacencias)):
            if self.__matrizAdjacencias[vert][x] >0:
                count+=1
        return count
    def __str__(self):
        termo_str =""
        for x in range(len(self.__matrizAdjacencias)):
            for i in range(len(self.__matrizAdjacencias)):
                if i == len(self.__matrizAdjacencias)-1:
                    termo_str += "{}|\n".format(self.__matrizAdjacencias[x][i])
                else:
                    termo_str += "{}|".format(self.__matrizAdjacencias[x][i])
        return termo_str
    def __repr__(self):
        aux = "GrafoMatriz("
        matriz_copia = np.array(self.__matrizAdjacencias)
        for x in range(len(matriz_copia)):
            for y in range(len(matriz_copia)):
                if int(matriz_copia[x][y]) == 1:
                    if int(matriz_copia[y][x]) == 1:
                        aux += "({},{})".format(x,y)
                        matriz_copia[x][y] = 0
                        matriz_copia[y][x] = 0
                    else:
                        aux += "({},{})".format(x,y)
                        matriz_copia[x][y] = 0
                elif int(matriz_copia[x][y]) >1:
                    if int(matriz_copia[y][x]) >1:
                        aux += "({},{},{})".format(x,y,matriz_copia[x][y])
                        matriz_copia[x][y] = 0
                        matriz_copia[y][x] = 0
                    else:
                        aux += "({},{},{})".format(x,y,matriz_copia[x][y])
                        matriz_copia[x][y] = 0
                else:
                    pass
        if self.__direcionado:
            aux+=", True)"
        else:
            aux +=")"
        return aux
    def tree(self):
        aux = []
        if self.__E != len(self.__V)-1:
            return False
        else:
            for x in range(len(self.__matrizAdjacencias)):
                grau = self.indegree(x)
                if grau == 2:
                    grau = self.outdegree(x)
                    if grau == 2:
                        aux.append(x)
            if len(aux) == len(self.__matrizAdjacencias):
                return False
            else:
                return True
def dfs(graph):
    '''
    Função que faz uma busca em profundidade do Grafo
    :param graph: Grafo a ser efetuado a busca
    :return: uma lista com todos os vértices antecessores em ordem de pesquisa
    '''
    status = graph.typegraph
    #Se o grafo for GrafoMatriz, será status ==0, caso não, entrará no else e irá ocorrer uma busca para o GrafoLista
    if status == 0:
        matriz_copia = np.array(graph.matriz)
        aux = 0
        visit = [False] * graph.V
        boolean = True
        vert_ant = []
        antecessor = 0
        adj = 0
        while boolean:
            count = 0
            if not visit[aux]:
                visit[aux] = True
                if aux not in vert_ant:
                    vert_ant.append(aux)
                for x in range(len(matriz_copia)):
                    if matriz_copia[aux][x] > 0:
                        count += 1
                        adj = x
                        matriz_copia[aux][x] = -1
                if count == 0:
                    aux = antecessor
                else:
                    antecessor = aux
                    aux = adj
            else:
                antecessor -= 1
                aux = antecessor
            if antecessor == -1:
                boolean = False
                return vert_ant
    else:
        listaadj = graph.listaadj
        aux = 0
        size = graph.V

        visit = [False] * size
        boolean = True
        vert_ant = []
        antecessor = 0
        adj = 0
        if graph.weight:
            while boolean:
                count = 0
                if not visit[aux]:
                    visit[aux] = True
                    if aux not in vert_ant:
                        vert_ant.append(aux)
                    for x in range(len(listaadj[aux])):
                        count += 1
                        adj = listaadj[aux][x][0]
                    antecessor = aux
                    aux = adj
                else:
                    antecessor -= 1
                    aux = antecessor
                if antecessor == -1:
                    boolean = False
                    return vert_ant
        else:
            while boolean:
                count = 0
                if not visit[aux]:
                    visit[aux] = True
                    if aux not in vert_ant:
                        vert_ant.append(aux)
                    for x in range(len(listaadj[aux])):
                        count += 1
                        adj = listaadj[aux][x]
                    antecessor = aux
                    aux = adj
                else:
                    antecessor -= 1
                    aux = antecessor
                if antecessor == -1:
                    boolean = False
                    return vert_ant
def bfs(graph, vert):
    '''
    Função que realize uma busca em largura no grafo na tentativa de achar um vértice dado como parametro
    :param graph: Grafo a ser lido na busca
    :param vert: Vértice que será utilizado como parametro na busca
    :return: Retorna a lista de vértices que foi checado para achar o vértice em questão, caso dê erro será levantado um Value Error
    '''
    status = graph.typegraph
    #Status == 0 será GrafoMatriz, else entrará no GrafoLista
    if status == 0:
        boolean = True
        count = 0
        visit = [False]*graph.V
        vert_ant = []
        try:
            while boolean:
                if not visit[count]:
                    visit[count] = True
                    if count not in vert_ant:
                        vert_ant.append(count)
                    for x in range(len(graph.matriz)):
                        if graph.matriz[count][x] >0:
                            if x == vert:
                                boolean = False
                else:
                    count +=1
        except:
            raise ValueError
        return vert_ant
    else:
        listaadj = graph.listaadj
        size = graph.V
        visit = [False] * size
        boolean = True
        vert_ant = []
        antecessor = 0
        adj = 0
        count = 0
        if graph.weight:
            try:
                while boolean:
                    if not visit[count]:
                        visit[count] = True
                        if count not in vert_ant:
                            vert_ant.append(count)
                        for x in range(len(listaadj[count])):
                            if listaadj[count][x][0] == vert:
                                boolean = False
                    else:
                        count +=1
            except:
                raise ValueError
            return vert_ant
        else:
            try:
                while boolean:
                    if not visit[count]:
                        visit[count] = True
                        if count not in vert_ant:
                            vert_ant.append(count)
                        for x in range(len(listaadj[count])):
                            if listaadj[count][x][0] == vert:
                                boolean = False
                    else:
                        count +=1
            except:
                raise ValueError
            return vert_ant