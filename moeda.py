class Moeda:
    def __init__(self, valor: float = 0.0, taxa: float = 1.0):
        self._valor = valor
        self._taxa = taxa
        
    @property
    def get_valor(self):
        return self._valor
    
    @get_valor.setter
    def get_valor(self, valor: float):
        self._valor = valor
        
        
    # --------------------------------------------------------------
        
    @property
    def get_taxa(self):
        return self._taxa
    
    @get_taxa.setter
    def get_taxa(self, taxa: float):
        self._taxa = taxa
        
    def converter(self):
        return round(self._valor * self._taxa, 2)