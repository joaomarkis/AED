"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
"""""


class _No:
    def __init__(self,texto = None):
        self.text = texto
        self.value = []
        self.children = {}
    def __iter__(self):
        return iter(self.children.values())

class Trie:
    def __init__(self):
        self.__root = _No()
        self.lenght = 0

    def insert(self, texto):
        word = str(texto)
        aux = self.__root
        for ch in word:
            if ch not in aux.children:
                aux.children[ch] = _No(ch)
            aux = aux.children[ch]
        aux.value.append(texto.documento)
        self.lenght +=1
    def search(self, texto):
        word = str(texto)
        aux = self.__root
        for ch in word:
            if ch not in aux.children:
                return False
            aux = aux.children[ch]
        if aux.value != None:
            return aux.value




