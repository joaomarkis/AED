"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
"""""

class NGram:
    def __init__(self,indicador,documento,n):
        self.__documento_referencia = documento
        self.__indice = indicador
        self.__n = n
    @property
    def indice(self):
        return self.__indice
    @property
    def n(self):
        return self.__n
    @property
    def documento(self):
        return self.__documento_referencia

    def __str__(self):
        termo_str = " "
        #busca o ngram baseado no indice dentro da lista de palavras do documento, gerando um termo str
        for x in range(self.__indice[0],self.__indice[1]):
            if x+1 == self.__indice[1]:
                termo_str = termo_str+"{}".format(self.__documento_referencia.lista_np[x])
            else:
                termo_str = termo_str+"{} ".format(self.__documento_referencia.lista_np[x])
        return termo_str

    def __repr__(self):
        termo_str = "Ngram({},{},{})".format(self.__indice, self.__documento_referencia, self.__n)
        return termo_str