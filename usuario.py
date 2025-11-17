class Usuario:
    def __init__(self, nome:str="", email:str = ""): # self: indica que pertence a classe
        self.login = nome
        self.senha = email

    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, nome):
        if not nome.strip() and nome == "":
            print("Nome inválido")
        else:
            self._login = nome
    
    # --------------------------------------------

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        if not senha.strip() and senha == "":
            print("Nome inválido")
        else:
            self._senha = senha

    def RealizarLogin(self, usuario, senha):
        if usuario == "usuario" and senha == "123":
            return True, f"Seja bem vindo {self.login}"
        else:
            return False, "Login/Senha Invalido"
        
