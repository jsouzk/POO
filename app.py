import streamlit as st
from imc import IMC
from moeda import Moeda

def login():
    st.title("Tela de Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        if usuario == "adm" and senha == "123":
            st.session_state['Logado'] = True
            st.success("Login realizado com sucesso!")
        else:
            st.error("Usuário ou senha incorretos.")
            
def Home():
    st.sidebar.title("Menu")
    opcao = st.sidebar.selectbox("Escolha uma opção:", ["IMC", "Conversor de Moeda"])
    
    if opcao == "IMC":
        st.header("Calcular IMC")
        peso = st.number_input("Digite seu peso (kg):", min_value=0.0, format="%.2f")
        altura = st.number_input("Digite sua altura (m):", min_value=0.0, format="%.2f")
        
        if st.button("Calcular IMC"):
            imc = IMC()
            imc.set_peso = peso
            imc.set_altura = altura
            resultado = imc.calcular_imc()
            if resultado:
                st.success(f"Seu IMC é: {resultado}")
            else:
                st.error("Dados invalidos")
                
    elif opcao == "Conversor de Moeda":
        st.header("Conversor de Moeda")
        valor = st.number_input("Digite o valor em Reais (R$):", min_value=0.0, format="%.2f")
        taxa = st.number_input("Digite a taxa de conversão:", min_value=0.0, format="%.4f")
        
        if st.button("Converter"):
            moeda = Moeda()
            moeda.set_valor = valor
            moeda.set_taxa = taxa
            resultado = moeda.converter()
            if resultado:
                st.success(f"Valor convertido: {resultado}")
            else:
                st.error("Dados invalidos")
                
if 'Logado' not in st.session_state:
    st.session_state['Logado'] = False
if not st.session_state['Logado']:
    login()
else:
    Home()