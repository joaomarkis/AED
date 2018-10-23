"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
"""""

import os
from Documento import Documento
import numpy as np

class Corpus:
    def __init__(self):
        path = "dados/src"
        temp = os.listdir(path)
        self.__list_src_title = np.array(temp)
        self.__list_document_src = np.empty(len(self.__list_src_title), dtype=object)
        for x in range(len(self.__list_src_title)):
            self.__list_document_src[x] = Documento(path+"/"+self.__list_src_title[x])
        path = "dados/susp"
        temp = os.listdir(path)
        self.__list_susp_title = np.array(temp)
        self.__list_document_susp = np.empty(len(self.__list_susp_title), dtype=object)
        for x in range(len(self.__list_susp_title)):
            self.__list_document_susp[x] = Documento(path+"/"+self.__list_susp_title[x])
    @property
    def list_src_title(self):
        return self.__list_src_title
    @property
    def list_document_src(self):
        return self.__list_document_src
    @property
    def list_susp_title(self):
        return self.__list_susp_title
    @property
    def list_document_susp(self):
        return self.__list_document_susp
    def verificarPlagio(self, document):
        limiar = 0.6
        cp_copy = []
        document_source = []
        document.gerarNGrams(2)
        for x in range(len(self.__list_document_src)):
            self.__list_document_src[x].gerarNGrams(2)
            cp = document.contencao(self.__list_document_src[x])
            if cp > limiar:
                cp_copy.append(cp)
                document_source.append(self.__list_src_title[x])
        quantidade = len(cp_copy) - 1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(quantidade):
                if cp_copy[i] < cp_copy[i + 1]:
                    cp_copy[i+1], cp_copy[i] = cp_copy[i], cp_copy[i+1]
                    document_source[i+1], document_source[i] = document_source[i], document_source[i+1]
                    ordenado = False
        print(document_source)
        return document_source
