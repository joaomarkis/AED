import numpy as np
import string
import lista_duplamente_encadeada as l
from NGram import NGram
class Documento:
    def __init__(self, titulo):
        self.__texto = titulo
        self.__lista = None
        arquivo = open(titulo, "r", encoding="utf-8")
        self.__texto = arquivo.read()
        self.__texto = "".join(x for x in self.__texto if x not in string.punctuation)
        self.__lista_np = np.array(self.__texto)
        arquivo.close()
        
    @property
    def lista(self):
        return self.__lista
    @property
    def texto(self):
        return self.__texto
    @property
    def lista_np(self):
        return self.__lista_np
    def gerarNGrams(self, n):
            self.__lista = l.DListaEncadeada()
            entrada = self.__texto.split()
            lista_termos = np.empty(len(entrada)-n+1, dtype=object)
            for x in range(len(entrada)-n+1):
                lista_termos[x] = entrada[x:x+n]
            for x in range(len(lista_termos)):
                self.__lista.anexar(NGram(lista_termos[x], n))
    def contencao(self, documento):
        cp = 0
        for x in self.lista:
            for i in (documento.lista):
                if x.termo == i.termo:
                    cp +=1
        cp = cp/len(self.__lista)
        return cp
