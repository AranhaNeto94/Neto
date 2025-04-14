import streamlit as st
import json
import requests

# Título da aplicação
st.title("MODELO DE PREDIÇÃO DE RECEITA")

# Inputs do usuário
st.write("Tempo de experiência do profissional (em anos):")
tempo_de_experiencia = st.slider("Tempo de Experiência (anos)", min_value=0.0, max_value=30.0, value=5.0, step=0.5)

st.write("Número de vendas realizadas:")
numero_de_vendas = st.slider("Número de Vendas", min_value=0, max_value=1000, value=100, step=10)

st.write("Fator sazonal (ex: 'baixo', 'médio', 'alto'): ")
fator_sazonal = st.selectbox("Fator Sazonal", options=["baixo", "médio", "alto"])

# Dicionário para mapear o fator sazonal para o valor codificado correto (pelo LabelEncoder)
fatores_sazonais = {"baixo": 0, "médio": 1, "alto": 2}

# Verifica se o fator sazonal está no dicionário e converte para o valor inteiro
if fator_sazonal in fatores_sazonais:
    fator_sazonal_codificado = fatores_sazonais[fator_sazonal]
else:
    st.error("Valor inválido para o fator sazonal.")
    fator_sazonal_codificado = None

# Montar dicionário com as features
input_features = {
    "tempo_de_experiencia": tempo_de_experiencia,
    "numero_de_vendas": numero_de_vendas,
    "fator_sazonal": fator_sazonal_codificado
}

# Botão de predição
if st.button('Estimar Receita'):
    if fator_sazonal_codificado is not None:  # Verifica se o fator sazonal foi corretamente codificado
        try:
            # Enviar dados para a API
            response = requests.post("http://127.0.0.1:8000/predict", data=json.dumps(input_features))
            result = response.json()

            if "receita_em_reais" in result:
                receita = round(result["receita_em_reais"], 2)
                st.subheader(f"A RECEITA ESTIMADA É DE R$ {receita}")
            else:
                st.error(f"Erro: {result.get('erro', 'Resposta inesperada da API')}")
        except Exception as e:
            st.error(f"Erro ao conectar à API: {e}")
    else:
        st.error("Não foi possível processar o fator sazonal.")
