# 🦠 Calculadora Epidêmica - Modelo SIR

Este projeto é um simulador matemático desenvolvido em **Python** que utiliza o modelo epidemiológico **SIR** (Suscetíveis, Infectados e Recuperados) para modelar e visualizar a difusão de doenças infectocontagiosas em uma população.

---

## 📉 Visão Geral do Projeto
O objetivo desta calculadora é prever a evolução de uma epidemia ao longo do tempo através de um sistema de Equações Diferenciais Ordinárias (EDOs). O modelo divide a população em três compartimentos:
- **S (Suscetíveis):** Indivíduos saudáveis que podem contrair a doença.
- **I (Infectados):** Indivíduos que contraíram a doença e podem transmiti-la.
- **R (Recuperados):** Indivíduos que se curaram e adquiriram imunidade ou faleceram.

A ferramenta permite que pesquisadores e estudantes simulem diferentes cenários mudando a agressividade da doença e a velocidade de recuperação.

---

## 🛠️ Funcionalidades da Calculadora
A interface foi projetada para ser totalmente interativa, permitindo os seguintes ajustes:

- **População Total (N):** Define o tamanho da comunidade sendo estudada.
- **Infectados Iniciais (I0):** Define quantos indivíduos iniciam a propagação do vírus.
- **Taxa de Transmissão (β - Beta):** Controla a probabilidade de contágio por contato. Quanto maior, mais rápido o vírus se espalha.
- **Taxa de Recuperação (γ - Gamma):** Define a velocidade com que os doentes saem do grupo de infectados. (Ex: se a doença dura 10 dias, o Gamma é 0.1).
- **Tempo de Simulação:** Slider para definir quantos dias a projeção deve cobrir.
- **Gráfico Interativo (Plotly):** Permite passar o mouse para ver os números exatos de cada dia.
- **Gráfico Estático (Matplotlib):** Uma visualização científica clássica para análise rápida de tendências.

---

## 💻 Tecnologias Usadas
O projeto utiliza o que há de mais moderno no ecossistema científico do Python:

- [**Python 3.x**](https://www.python.org/): Linguagem base do projeto.
- [**Streamlit**](https://streamlit.io/): Framework utilizado para criar a Dashboard moderna e interativa.
- [**NumPy**](https://numpy.org/): Para processamento de vetores e cálculos matemáticos.
- [**SciPy**](https://scipy.org/): Especificamente a função `odeint` para resolver as equações diferenciais.
- [**Pandas**](https://pandas.pydata.org/): Para estruturar os resultados da simulação em tabelas.
- [**Plotly**](https://plotly.com/): Para a geração de gráficos dinâmicos e responsivos.
- [**Matplotlib**](https://matplotlib.org/): Para a geração de gráficos científicos estáticos.

---

## 🤖 Colaboração com Inteligência Artificial
Este projeto foi desenvolvido com o auxílio do Gemini, que atuou em duas frentes complementares:

- **Papel como Engenheiro de Software Python Sênior:** O Gemini foi responsável por estruturar a arquitetura do código, garantindo a separação limpa entre a lógica matemática (`model.py`) e a interface de usuário (`app.py`), além de aplicar boas práticas de desenvolvimento e visualização de dados.
- **Papel como Pesquisador Acadêmico:** Para a documentação e fundamentação do projeto, o Gemini redigiu o artigo científico anexo (`ARTIGO_CIENTIFICO.md`), garantindo o rigor técnico na explicação das equações diferenciais e na interpretação metodológica do modelo SIR.

---

## 🤝 Abordagem Humano-IA
A construção deste repositório ilustra na prática como a colaboração entre humanos e IA pode transformar projetos educacionais e de pesquisa. 

Ferramentas de IA atuam como parceiras poderosas na engenharia de software, automatizando a escrita de códigos complexos e a configuração de interfaces, o que permite ao humano focar na concepção da ideia, no ajuste das regras de negócio (neste caso, as variáveis epidemiológicas) e na validação crítica dos resultados. Essa sinergia demonstra que a adoção de assistentes virtuais não substitui o pensamento analítico, mas atua como um catalisador que eleva a qualidade e a velocidade do desenvolvimento tecnológico e da pesquisa acadêmica.

---

## 🚀 Como Executar
Mesmo que você esteja visualizando o código, caso deseje rodar o projeto futuramente, siga estes passos:

1. **Instale as bibliotecas necessárias:**
   ```bash
   pip install -r requirements.txt

2. **Inicie o servidor do Streamlit:**
   ```bash
   streamlit run app.py

3. **Acesse no navegador:**
   http://localhost:8501 


