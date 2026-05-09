import numpy as np
import pandas as pd
from scipy.integrate import odeint

def sir_derivadas(y, t, N, beta, gamma):
    """
    Define o sistema de equações diferenciais para o modelo SIR.
    """
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

def simular_sir(N, I0, beta, gamma, dias):
    """
    Executa a simulação do modelo SIR e retorna os dados organizados em um DataFrame Pandas.
    """
    # População inicial
    R0 = 0  # Começamos com zero recuperados
    S0 = N - I0 - R0 # O resto da população é suscetível
    
    # Vetor de condições iniciais
    y0 = S0, I0, R0
    
    # Grid de tempo (em dias)
    t = np.linspace(0, dias, dias)
    
    # Integra as equações diferenciais usando odeint (SciPy)
    resultado = odeint(sir_derivadas, y0, t, args=(N, beta, gamma))
    S, I, R = resultado.T
    
    # Organiza os dados utilizando Pandas
    df = pd.DataFrame({
        'Dia': t,
        'Suscetíveis': S,
        'Infectados': I,
        'Recuperados': R
    })
    
    return df