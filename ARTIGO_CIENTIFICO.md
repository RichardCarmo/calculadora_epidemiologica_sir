# Desenvolvimento de uma Ferramenta de Simulação Computacional para Modelagem Epidemiológica SIR

**Área:** Epidemiologia Matemática / Ciência da Computação  
**Data:** Maio de 2026 

---

### 1. Resumo
Este trabalho apresenta o desenvolvimento de uma calculadora epidemiológica baseada no modelo determinístico clássico SIR (Suscetíveis-Infectados-Recuperados). O software foi implementado inteiramente na linguagem Python, utilizando bibliotecas avançadas de computação científica para resolver sistemas de equações diferenciais ordinárias (EDOs). O objetivo principal do projeto é fornecer uma interface visual e altamente interativa que permita a simulação de diferentes cenários de contágio a partir do ajuste de parâmetros fundamentais, como o tamanho da população, as taxas de transmissão e as taxas de recuperação. Os resultados demonstram que a ferramenta é eficaz para a visualização clara da dinâmica de formação dos picos de infecção, facilitando a compreensão de conceitos complexos como a imunidade de rebanho e o achatamento da curva.

---

### 2. Introdução
A modelagem matemática é o processo sistemático de representar fenômenos físicos, biológicos ou sociais do mundo real por meio de equações e estruturas lógicas. Essa prática metodológica permite simplificar sistemas altamente complexos — desde as flutuações do mercado financeiro até o crescimento de populações ecológicas — traduzindo-os em variáveis e parâmetros quantificáveis. Ao converter a realidade para a linguagem matemática, os pesquisadores adquirem a capacidade não apenas de descrever o que já foi observado empiricamente, mas, fundamentalmente, de prever cenários futuros sob diferentes condições. Essa capacidade preditiva transforma a matemática em um laboratório virtual, onde é possível testar hipóteses e realizar simulações em ambientes estritamente controlados, sem os riscos ou custos de um experimento real.



No contexto específico das ciências da saúde, a modelagem matemática aplicada a doenças infecciosas estabeleceu-se como uma ferramenta indispensável, fato que ganhou notória visibilidade global e importância estratégica durante a recente pandemia de COVID-19. A epidemiologia matemática comumente utiliza os chamados "modelos compartimentais" para rastrear como um patógeno flui e se dispersa através de uma comunidade ao longo do tempo. 

O propósito de modelar a difusão dessas doenças é duplo. Primeiro, visa-se compreender o comportamento biológico intrínseco do vírus, sua agressividade e a velocidade de propagação em populações virgens de imunidade. Segundo, a modelagem fornece subsídios quantitativos cruciais para a tomada de decisão por parte de gestores de políticas públicas. Através de simulações computacionais precisas, torna-se viável prever o impacto de uma epidemia semanas ou meses antes que ela atinja o seu ápice. Isso orienta o planejamento estratégico para a implementação de medidas mitigadoras de forma antecipada — como campanhas de vacinação, fechamento temporário de fronteiras ou distanciamento social —, garantindo a alocação otimizada de recursos e evitando o colapso estrutural das redes e sistemas de saúde.

---

### 3. Metodologia
A arquitetura algorítmica e a base teórica desta calculadora residem no modelo clássico proposto originalmente por Kermack e McKendrick em 1927. Neste modelo compartimental, a população total ($N$) é assumida como constante e é segmentada em três grupos (compartimentos) mutuamente exclusivos. A transição de indivíduos entre esses estados é governada de forma contínua no tempo ($t$) por um sistema de Equações Diferenciais Ordinárias (EDOs):

1. **Variação de Suscetíveis ($dS/dt$):** Descreve a taxa decrescente com que indivíduos saudáveis e sem imunidade contraem a infecção ao entrarem em contato com indivíduos já infectados.
   $$\frac{dS}{dt} = -\frac{\beta S I}{N}$$

2. **Variação de Infectados ($dI/dt$):** Representa o saldo transitório entre os novos contágios (que entram neste compartimento) e os indivíduos que se curam da doença (que saem deste compartimento).
   $$\frac{dI}{dt} = \frac{\beta S I}{N} - \gamma I$$

3. **Variação de Recuperados ($dR/dt$):** Quantifica o acúmulo irreversível de indivíduos que venceram a infecção e adquiriram imunidade celular de longo prazo.
   $$\frac{dR}{dt} = \gamma I$$

Para a implementação técnica do software, utilizou-se o integrador numérico `odeint` pertencente à biblioteca **SciPy**. O **NumPy** foi empregado para a geração dos espaços vetoriais e a biblioteca **Pandas** para a estruturação dos dados resultantes.

---

### 4. Resultados e Discussão
A concepção de uma interface gráfica dinâmica através do framework **Streamlit** revelou-se um diferencial crítico para a interpretação prática dos dados. Diferente de scripts computacionais estáticos, a calculadora desenvolvida permite o ajuste em tempo real dos parâmetros vitais: a Taxa de Transmissão ($\beta$) e a Taxa de Recuperação ($\gamma$).

Durante os testes operacionais, observou-se claramente que pequenas reduções manuais no parâmetro $\beta$ (simulando medidas de isolamento) resultam em deslocamentos drásticos e positivos no achatamento da curva epidemiológica. A disposição simultânea das projeções numéricas através de painéis interativos (**Plotly**) e perspectivas estáticas (**Matplotlib**) auxilia o usuário a identificar empiricamente a linha de saturação de um sistema de saúde.

---

### 5. Conclusão
O desenvolvimento desta calculadora epidemiológica evidencia o potencial interdisciplinar da união entre a matemática aplicada e as modernas práticas de engenharia de software. Conclui-se que simuladores computacionais acessíveis contribuem materialmente para a saúde pública e para a academia, atuando tanto como instrumentos de predição quanto como recursos educativos de alto impacto. Embora o modelo SIR clássico seja uma simplificação, sua eficiência computacional fornece um alicerce robusto para o raciocínio clínico e o planejamento governamental perante crises sanitárias.

---
**Palavras-chave:** Modelagem Matemática, Equações Diferenciais, Python, Modelo SIR, Epidemiologia Computacional.