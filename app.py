import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from model import simular_sir

# Configuração da página do Streamlit
st.set_page_config(page_title="Calculadora SIR", layout="wide")

st.title("🦠 Calculadora Epidêmica - Modelo SIR")
st.markdown("Dashboard interativa para modelar a difusão de doenças infectocontagiosas.")

# -----------------
# Barra Lateral (Menu)
# -----------------
st.sidebar.header("⚙️ Ajuste de Parâmetros")

N = st.sidebar.number_input("População Total (N)", min_value=1000, value=100000, step=10000)
I0 = st.sidebar.number_input("Infectados Iniciais (I0)", min_value=1, value=10, step=1)

st.sidebar.markdown("---")
beta = st.sidebar.slider("Taxa de Transmissão (β)", min_value=0.0, max_value=2.0, value=0.3, step=0.01)
gamma = st.sidebar.slider("Taxa de Recuperação (γ)", min_value=0.0, max_value=1.0, value=0.1, step=0.01)
dias = st.sidebar.slider("Tempo de Simulação (Dias)", min_value=10, max_value=365, value=160, step=10)

# -----------------
# Simulação
# -----------------
# Chama o nosso modelo estruturado com NumPy/SciPy e retorna um DataFrame Pandas
df_resultados = simular_sir(N, I0, beta, gamma, dias)

# -----------------
# Visualizações
# -----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gráfico Interativo (Plotly)")
    # Uso do Plotly para uma visualização moderna e interativa
    fig_plotly = px.line(df_resultados, x='Dia', y=['Suscetíveis', 'Infectados', 'Recuperados'],
                         color_discrete_map={
                             'Suscetíveis': '#1f77b4', # Azul
                             'Infectados': '#d62728',  # Vermelho
                             'Recuperados': '#2ca02c'  # Verde
                         })
    fig_plotly.update_layout(yaxis_title="População", legend_title_text="Status")
    st.plotly_chart(fig_plotly, use_container_width=True)

with col2:
    st.subheader("Gráfico Estático (Matplotlib)")
    # Uso do Matplotlib para visualização clássica/científica
    fig_mat, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(df_resultados['Dia'], df_resultados['Suscetíveis'], label='Suscetíveis', color='#1f77b4')
    ax.plot(df_resultados['Dia'], df_resultados['Infectados'], label='Infectados', color='#d62728')
    ax.plot(df_resultados['Dia'], df_resultados['Recuperados'], label='Recuperados', color='#2ca02c')
    ax.set_xlabel('Dias')
    ax.set_ylabel('População')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig_mat)

# -----------------
# Dados Brutos
# -----------------
st.subheader("Tabela de Dados (Pandas)")
st.dataframe(df_resultados, use_container_width=True)