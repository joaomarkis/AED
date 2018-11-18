import numpy as np

class GrafoLista:
    def __init__(self, grupo, direcionado=False):
        self.__V = []
        for x in grupo:
            if x[0] not in self.__V:
                self.__V.append(x[0])
            elif x[1] not in self.__V:
                self.__V.append(x[1])
        self.__listaAdjacencias = [[] for i in range(len(self.__V))]
        self.__E = 0
        self.__direcionado = direcionado
        for i in grupo:
            self.inserirAresta(i)

    #Retorna o número de vertices
    def V(self):
        return len(self.__V)
    #Retorna o número de arestas
    def E(self):
        return self.__E
    #Adiciona as arestas para conectar os vértices
    def inserirAresta(self, tuplex):
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

    #Retorna uma lista com os vertices adjacentes a X
    def adj(self, x):
        return self.__listaAdjacencias[x]
    def transformGrafo(self):
        aux =[]
        print(self.__listaAdjacencias)
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
        return GrafoMatriz(aux)
    def indegree(self, vertice):
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
                print(self.__listaAdjacencias[x])
                if x == vertice:
                    continue
                elif vertice in self.__listaAdjacencias[x]:
                    count +=1
        return count
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
class GrafoMatriz:
    def __init__(self, grupo, direcionado=False):
        self.__V = []
        for x in grupo:
            if x[0] not in self.__V:
                self.__V.append(x[0])
            elif x[1] not in self.__V:
                self.__V.append(x[1])
        self.__matrizAdjacencias = np.arange(len(self.__V), dtype=object)
        for x in range(len(self.__matrizAdjacencias)):
            self.__matrizAdjacencias = np.array([0]*len(self.__V)*len(self.__V)).reshape(len(self.__V),len(self.__V))
        self.__E = 0
        self.__direcionado = direcionado
        for i in grupo:
            self.inserirAresta(i)
        self.str_vers = str(grupo)
    @property
    def matriz(self):
        return self.__matrizAdjacencias
    #Retorna o número de vertices
    def V(self):
        return len(self.__V)
    #Retorna o número de arestas
    def E(self):
        return self.__E
    #Adiciona as arestas para conectar os vértices
    def inserirAresta(self, tuplex):
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
        aux = []
        matriz_copia = np.array(self.__matrizAdjacencias)
        print(matriz_copia)
        for x in range(len(matriz_copia)):
            for y in range(len(matriz_copia)):
                if int(matriz_copia[x][y]) == 1:
                    print("dale")
                    if int(matriz_copia[y][x]) == 1:
                        aux.append((x,y))
                        matriz_copia[x][y] = 0
                        matriz_copia[y][x] = 0
                    else:
                        aux.append((x,y))
                        matriz_copia[x][y] = 0
                elif int(matriz_copia[x][y]) >1:
                    print("oi")
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
        print(aux)
        aux = tuple(aux)
        return GrafoLista(aux, self.__direcionado)
    def indegree(self, vert):
        count = 0
        print(self.__matrizAdjacencias)
        for x in range(len(self.__matrizAdjacencias)):
            if x == vert:
                continue
            else:
                print(self.__matrizAdjacencias[x][vert])
                if self.__matrizAdjacencias[x][vert]>0:
                    count+=1
        return count
    def outdegree(self, vert):
        count = 0
        print(self.__matrizAdjacencias)
        for x in range(len(self.__matrizAdjacencias)):
            if self.__matrizAdjacencias[vert][x] >0:
                count+=1
        return count
    def dfs(self,vert):
        matriz_copia = np.array(self.__matrizAdjacencias)
        aux = vert
        visit = [False]*len(self.__V)
        boolean = True
        vert_ant = []
        antecessor = 0
        adj = 0
        while boolean:
            count = 0
            print(matriz_copia)
            if not visit[aux]:
                visit[aux] = True
                if aux not in vert_ant:
                    vert_ant.append(aux)
                for x in range(len(matriz_copia)):
                    if matriz_copia[aux][x] >0:
                        count +=1
                        adj = x
                        matriz_copia[aux][x] = -1
                if count == 0:
                    aux = antecessor
                else:
                    antecessor = aux
                    aux = adj
            else:
                antecessor -=1
                aux = antecessor
            if antecessor == -1:
                boolean = False
                return vert_ant