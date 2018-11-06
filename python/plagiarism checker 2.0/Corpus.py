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
import trie as t


class Corpus:
    #Inicia o código gerando listas com todos os títulos dos arquivos
    def __init__(self):
        self.__t_trie = t.Trie()
        temp = os.listdir("dados/src")
        self.__list_src_title = np.array(temp)
        self.__list_document_src = np.empty(len(self.__list_src_title), dtype=object)
        temp = os.listdir("dados/susp")
        self.__list_susp_title = np.array(temp)
        self.__list_document_susp = np.empty(len(self.__list_susp_title), dtype=object)
        self.__readFiles()

    def __readFiles(self):
        ''' Lê e gera todos os documentos. NGrams dos documentos base(docsrc) também são gerados, assim como a árvore trie.'''
        for x in range(len(self.__list_src_title)):
            self.__list_document_src[x] = Documento("dados/src/"+self.__list_src_title[x])
            self.__list_document_src[x].gerarNGrams(2)
            self.__list_document_src[x].title = self.__list_src_title[x]
            for x in self.__list_document_src[x].lista:
                self.__t_trie.insert(x)
        for x in range(len(self.__list_susp_title)):
            self.__list_document_susp[x] = Documento("dados/susp/"+self.__list_susp_title[x])

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

    def verificarPlagio(self, document, limiar):
        '''
        Verifica o plágio entre um documento suspeito e os de base(source)
        :param document: documento suspeito a ser analisado
        :param limiar: limite de similaridade entre os dois documentos.
        :return: retorna a lista de títulos que correspondem aos possíveis documentos que serviram de base para o plágio. '''
        cp,document_source = self.contencao(document, limiar)
        self.sortTitle(cp, document_source)
        return document_source

    def contencao(self, document,limiar):
        '''
        Executa a verificação de similaridade entre o documento suspeito com os de base, pesquisando o ngram
        existente do docsusp dentro da árvore trie que contém os ngram dos docsrc.
        :param document: documento suspeito(docsusp) que vai ser comparado aos documentos base(docsrc)
        :param limiar: limite de similaridade entre os dois docs
        :return: retorna uma lista com títulos acima do limite e uma lista com suas respectivas contenções.
        '''
        cp = []
        document_source = []
        document.gerarNGrams(2)
        #pesquisa dentro da árvore trie que tem os ngrams do source se existe ngrams similares ao documento suspeito
        for x in document.lista:
            #recebe os valores que contém as listas de documentos sobre o ngram pesquisado
            values = self.__t_trie.search(x)
            #se o ngram for encontrado, os documentos que contém ele vão ser armazenados em uma lista
            if values != False:
                for i in values:
                    document_source.append(i.title)
        #contagem de quantas vezes cada documento foi encontrado, dividido pelo tamanho do ngram suspeito, gerando a contenção
        doc_src = {x: document_source.count(x)/len(document.lista) for x in set(document_source)}
        document_source = []
        #dicionário com todos os títulos e suas contenções como valor, resgatamos apenas os titulos que tem valores acima do limiar
        for key in doc_src.keys():
            if doc_src[key]>limiar:
                document_source.append(key)
                cp.append(doc_src[key])
        return cp, document_source

    def sortTitle(self, cp, document_source):
        '''
        Ordena os títulos baseado no seu valor de contenção, do maior para o menor.
        :param cp: recebe uma lista com os valores de contenção acima do limiar
        :param document_source: recebe uma lista com os títulos dos documentos base que estão acima do limiar
        :return: retorna a lista de títulos ordenada do maior grau de contenção para o menor
        '''
        quantidade = len(cp) -1
        ordenado = False
        while not ordenado:
            ordenado = True
            for i in range(quantidade):
                if cp[i] < cp[i + 1]:
                    cp[i+1], cp[i] = cp[i], cp[i+1]
                    document_source[i+1], document_source[i] = document_source[i], document_source[i+1]
                    ordenado = False
        #retorna uma lista com todos os documentos ordenados que possivelmente serviram de base para o plágio
        return document_source