"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
"""""


import numpy as np
import string
import lista_duplamente_encadeada as l
from NGram import NGram
class Documento:
    #inicia o método documento abrindo o arquivo e gerando uma lista com todas as palavras
    def __init__(self, titulo):
        self.__titulo = titulo
        self.__lista = None
        arquivo = open(titulo, "r", encoding="utf-8")
        self.__texto = arquivo.read()
        #retira todos os sinais indesejados
        self.__texto = "".join(x for x in self.__texto if x not in string.punctuation)
        self.__texto = self.texto.split()
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
    @property
    def title(self):
        return self.__titulo
    @title.setter
    def title(self, title):
        self.__titulo = title

    def gerarNGrams(self, n):
            ''' Gera os ngrams do documento no tamanho do parametro n, com base na técnica da janela deslizante'''
            self.__lista = l.DListaEncadeada()
            entrada = self.__texto
            #busca o range até o limite da lista de palavras -n+1 para não ficar com a formatação errada nos ngram
            for x in range(len(entrada)-n+1):
                #recebe o indice que se refere ao ngram, ao invés de armazenar palavras
                indice = (x,x+n)
                #referencia do documento que gerou o ngram
                doc = self
                #lista duplamente encadeada que armazena todos os ngram deste documento
                self.__lista.anexar(NGram(indice,doc,n))