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
        def 


    

    
