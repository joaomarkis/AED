"""""
Universidade Federal de Pernambuco - UFPE
Centro de Informática - CIn
IF969 - 2018.2
Autor: João Victor Marques dos Santos
E-mail: jvms@cin.ufpe.br
"""""


class _No:
    def __init__(self, item=None, anterior=None, proximo=None,):
        self.item = item
        self.ante = anterior
        self.prox = proximo
class DListaEncadeada:
    def __init__(self, *valor):
        self.__primeiro = self.__ultimo = _No()
        self.__Tamanho = 0
        if valor == ():
            self.vazio()
        for item in valor:
            self.anexar(item)
    def vazio(self):
        return self.__primeiro == self.__ultimo
    def __str__(self):
        termo_str ="["
        for x in range(self.__Tamanho):
            if x+1 == self.__Tamanho:
                termo_str = termo_str + "{}]".format(self.get_no(x).item)
            else:
                termo_str = termo_str + "{};".format(self.get_no(x).item)
        return termo_str
    def anexar(self,valor):
        self.__ultimo.prox = _No(valor, self.__ultimo, None)
        self.__ultimo = self.__ultimo.prox
        self.__Tamanho +=1
    def inserir(self, indice, valor):
        if indice == 0:
            aux = _No(valor, self.__primeiro, self.__primeiro.prox)
            self.__primeiro.prox = aux
            if self.vazio():
                self.__ultimo = aux
            else:
                aux.prox.ante = aux
            self.__Tamanho +=1
            del aux
        else:
            ref = self.get_no(indice-1)
            if ref == False:
                self.anexar(valor)
            else:
                aux = _No(valor, ref, ref.prox)
                ref.prox = aux
                if aux.prox is None:
                    self.__ultimo = aux
                else:
                    aux.prox.ante = aux
                self.__Tamanho +=1
                del aux
    def pop(self, index=None):
        if self.vazio():
            raise IndexError
        elif index+1 == self.__Tamanho:
            index = None
        elif index == None:
            aux = self.__ultimo
            self.__ultimo = aux.ante
            valor = aux.item
            self.__ultimo.prox = None
            del aux
            self.__Tamanho -=1
            return valor
        elif index >self.__Tamanho-1:
            raise IndexError
        else:
            ref = self.get_no(index)
            ref.ante.prox = ref.prox
            ref.prox.ante = ref.ante
            valor = ref.item
            del ref
            self.__Tamanho -=1
            return valor
    def remover(self,valor):
        if self.vazio():
            raise ValueError
        aux = self.__primeiro
        while aux.prox != None and aux.prox.item != valor:
            aux = aux.prox
        if aux.prox == None:
            raise ValueError
        elif aux.prox == self.__ultimo:
            self.__ultimo = aux
            self.__ultimo.prox = None
            self.__Tamanho -=1
            del aux
        else:
            ref = aux.prox
            valor = aux.prox.item
            ref.ante.prox = ref.prox
            ref.prox.ante = ref.ante
            if aux.prox == None:
                self.__ultimo = aux
            del ref
            self.__Tamanho -=1
            return valor
    def procurar(self,valor):
        aux = self.__primeiro
        termo = 0
        while aux.prox != None and aux.prox.item != valor:
            aux = aux.prox
            termo +=1
        if aux.prox == None:
            raise ValueError
        else:
            return termo
    def eliminar(self, valor):
        condicional = True
        while condicional:
            aux = self.__primeiro
            while aux.prox != None and aux.prox.item != valor:
                aux = aux.prox
            if aux.prox == None:
                condicional = False
            else:
                aux_temp = aux.prox
                valor = aux.prox.item
                aux.prox = aux_temp.prox
                if aux.prox == None:
                    self.__ultimo = aux
                del aux_temp
                self.__Tamanho -=1
    def copiar(self):
        return DListaEncadeada(*self)
    def trocar(self,index1,index2):
        node1 = self.get_no(index1)
        node2 = self.get_no(index2)
        node1.item,node2.item = node2.item, node1.item
    def estender(self, *args):
        for x in args:
            self.anexar(x)
    def __repr__(self):
        termo_str = "ListaDupla(["
        for x in range(self.__Tamanho):
            if x+1 == self.__Tamanho:
                termo_str = termo_str + "{}])".format(self.get_no(x).item)
            else:
                termo_str = termo_str + "{},".format(self.get_no(x).item)
        return termo_str
    def __len__(self):
        return self.__Tamanho
    def __getitem__(self, index):
        for x in range(self.__Tamanho):
            valor = self.get_no(index).item
        if valor == None:
            return ValueError
        return valor
    def __setitem__(self, index, valor):
        aux = self.get_no(index)
        if aux == False:
            raise IndexError
        else:
            aux.item = valor
    def __contains__(self, item):
        aux = self.__primeiro
        while aux != None and aux.item != item:
            aux = aux.prox
        if aux == None:
            return False
        else:
            return True
    def __iter__(self):
        self.__atual = self.__primeiro.prox
        return self
    def __next__(self):
        if self.__atual == None:
            raise StopIteration
        else:
            valor = self.__atual.item
            self.__atual = self.__atual.prox
            return valor

    def get_no(self,index):
        if index>self.__Tamanho:
            return False
        aux = self.__primeiro.prox
        for x in range(index):
            aux = aux.prox
        return aux
    @property
    def item(self):
        return self.__primeiro.item
    @property
    def prox(self):
        return self.__primeiro.prox
def concatenar(lista1,lista2):
    lista1.estender(*lista2)

