import streamlit as st

class Pessoa:
    def __init__(self, nome = str, ano_nascimento = int, peso = float, altura = float):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.peso = peso
        self.altura = altura
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    # --------------------------------
        
    @property
    def ano_nascimento(self):
        return self._ano_nascimento
    
    @ano_nascimento.setter
    def ano_nascimento(self, ano_nascimento):
        self._ano_nascimento = ano_nascimento
    
    # --------------------------------
        
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, peso):
        self._peso = peso
        
    # --------------------------------    
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura
    
    # Metodos 
    
    def calcular_idade(self, ano_atual):
        return ano_atual - self.ano_nascimento
    
    def calcular_imc(self):
        return self.peso / (self.altura * self.altura)
    
    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Normal"
        elif 25 <= imc < 29.9:
            return "Acima do peso"
        else:
            return "Obeso"
        
st.title("Calculadora de Idade e IMC")
nome = st.text_input("Nome:")
ano_nascimento = st.number_input("Ano de Nascimento:", min_value=1900, max_value=2025, step=1)
peso = st.number_input("Peso (kg):", min_value=0.0, step=0.1)
altura = st.number_input("Altura ( em M):", min_value=0.0, step=0.01)

if st.button("Calcular"):
    pessoa = Pessoa(nome, ano_nascimento, peso, altura)
    idade = pessoa.calcular_idade(2025)
    imc = pessoa.calcular_imc()
    classificacao_imc = pessoa.classificar_imc()
    
    st.success(f"Nome: {pessoa.nome}")
    st.success(f"Idade: {idade} anos")
    st.success(f"IMC: {imc:.2f}")
    st.success(f"Classificação do IMC: {classificacao_imc}")
else:
    st.error("Por favor, preencha os dados e clique em 'Calcular'.")