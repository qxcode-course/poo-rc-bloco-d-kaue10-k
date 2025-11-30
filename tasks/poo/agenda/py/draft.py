class Telefone:
    def __init__ (self, id, numero):
        self.id = id 
        self.numero = numero

    def __str__(self):
        return f"{self.id}:{self.numero}"


class Contato:
    def __init__(self, nome):
        self.nome = nome
        self.telefone = []
        self.favorito = false 
        

    def ad_telefone(self, id, numero):
        self.telefone.append(telefone(id, numero))

    def remover_telefone(self, id):
        self.telefone = [t for t in self.telefone if t.id != id]


    def __str__(self):
        fav = "*" if self.favorito else ""
        tel = ",".join(str(t) for t in self.telefone)
        return f"[{fav}] {self.nome} -> {tel}" 
    

class Agenda:
    def __init__(self):
        self.contatos = {}

    def add_contato(self, nome, telefone):
        if nome not in self.contatos:
            self.contato[nome] = contato = (nome)

        for id numero in telefone():
            self.contato[nome].add_telefone(id, numero)


    def mostrar(self):
        for nome in sorted(self.contato):
            print(self.contato[nome])


    def remover_contato(self):
        if nome in self.contato:
            del self.contato[nome]


    def remover_telefone(self, nome, id):
        if nome in self.contato:
            self.contato[nome].remover_telefone(id)
    








    

    
