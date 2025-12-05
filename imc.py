class IMC:
    def __init__(self, peso: float = 0.0, altura: float = 0.0):
        self._peso = peso
        self._altura = altura
        
    @property
    def get_peso(self):
        return self._peso
    
    @get_peso.setter
    def get_peso(self, peso: float):
        self._peso = peso
        
    
    # --------------------------------------------------------------
        
    @property
    def get_altura(self):
        return self._altura
    
    @get_altura.setter
    def get_altura(self, altura: float):
        self._altura = altura
        
    def calcular_imc(self):
        return round(self._peso / (self._altura ** 2), 2)
    
    
        
    