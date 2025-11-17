import streamlit as st

class Usuario:
    def __init__(self, login = str, senha = str):
        self.login = login
        self.senha = senha

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    # --------------------------------------------

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha


class Professor:
    def __init__(self, nome = str, matricula = int):
        self.nome = nome
        self.matricula = matricula

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    # ----------------------------------------------

    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula


class Aluno:
    def __init__(self, nome = str):
        self.nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
