# parte 1

class Carro:
    def __init__(self, modelo:str, ano:int):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0.0

    def acelerar(self, quantidade:float):
        self.velocidade += quantidade
        
        self.velocidade = self.velocidade if self.velocidade <= 180 else 180.0

    def desacelerar(self, quantidade: float):
        self.velocidade -= quantidade

        self.velocidade = self.velocidade if self.velocidade >= 0 else 0.0

carro = Carro("batmovel", 2025)

carro.acelerar(10.0)
carro.desacelerar(5.0)

print(f"velocidade final: {carro.velocidade}")

# parte 2

class CarroEletrico(Carro):
    def __init__(self, modelo:str, ano:int, autonomia_bateria=float):
        super().__init__(modelo, ano)
        self.autonomia_bateria = autonomia_bateria


