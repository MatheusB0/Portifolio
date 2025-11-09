import numpy as np
from scipy import stats 
import streamlit as st
def calcular(entrada):
    try:
        vetor = np.array([float(x.strip()) for x in entrada.split(",")])
        soma = np.sum(vetor)
        media = np.mean(vetor)
        mediana = np.median(vetor)
        minimo = np.min(vetor)
        maximo = np.max(vetor)
        moda = stats.mode(vetor).mode.item()
        
        st.metric("Soma", soma)
        st.metric("Média", media)
        st.metric("Mediana", mediana)
        st.metric("Moda", moda)
        st.metric("Mínimo", minimo)
        st.metric("Máximo", maximo)
        
        st.bar_chart(vetor)
    
    except Exception as e:
        st.error(f"Erro ao processar o vetor: {e}")