"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
"""""

class NGram:
    def __init__(self, texto, n=2):
        self.__n = n
        if len(texto) == self.__n:
            self.__termo = texto
        else:
            texto = texto.split()
            if len(texto) == self.__n:
                self.__termo = texto
            else:
                raise ValueError
    @property
    def termo(self):
        return self.__termo
    @property
    def n(self):
        return self.__n

    def __str__(self):
        termo_str = "["
        for x in range(len(self.__termo)):
            if x+1 == len(self.__termo):
                termo_str = termo_str+"{}]".format(self.__termo[x])
            else:
                termo_str = termo_str+"{},".format(self.__termo[x])
        return termo_str

    def __repr__(self):
        termo_str = "NGram("
        for x in range(len(self.__termo)):
            if x == 0:
                termo_str = termo_str + "''{} ".format(self.__termo[x])
            elif x+1 == len(self.__termo):
                termo_str = termo_str+"{}'',{})".format(self.__termo[x], self.__n)
            else:
                termo_str = termo_str+"{} ".format(self.__termo[x])
        return termo_str