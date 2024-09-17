# Criado apenas quando um sensor de temperatura é criado
class ArCondicionado():
    def __init__(self, id, ligado, qtd_resf):
        self.id = id
        self.ligado = ligado
        self.qtd_resf = qtd_resf
    
    def ligar(self):
        self.qtd_resf = True
        print(f"Ar condicionado {self.id} ligado.")

    def desligar(self):
        self.qtd_resf = False
        print(f"Ar condicionado {self.id} desligado.")
