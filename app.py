# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:11:46 2024

@author: jperezr
"""

import streamlit as st
import numpy as np

# Título de la aplicación
st.title("Prueba de Hipótesis sobre el Coeficiente de Correlación ρ")
st.write("Por: Javier Horacio Pérez Ricárdez")


st.write("Este cálculo se realiza utilizando las fórmulas proporcionadas para probar la hipótesis nula: \( H_0: ρ = 0 \)")

# Datos de ejemplo
x = np.array([11.1, 10.3, 12.0, 15.1, 13.7, 18.5, 17.3, 14.2, 14.8, 15.3])
y = np.array([10.9, 14.2, 13.8, 21.5, 13.2, 21.1, 16.4, 19.3, 17.4, 19.0])

# Calcular el coeficiente de correlación de Pearson
r = np.corrcoef(x, y)[0, 1]

# Número de pares de datos
n = len(x)

# Calcular Z usando la fórmula
Z = np.sqrt(n-3) / 2 * np.log((1 + r) / (1 - r))

# Calcular z usando la fórmula
z = np.sqrt(n-3) * Z

# Mostrar resultados
st.write(f"**Coeficiente de correlación de Pearson (r):** {r:.4f}")
st.write(f"**Valor de Z calculado:** {Z:.4f}")
st.write(f"**Estadístico z calculado:** {z:.4f}")

# Conclusión
z_critico = 1.96  # valor crítico para un nivel de significancia de 0.05 en una prueba bilateral
if abs(z) > z_critico:
    st.write("**Resultado:** Se rechaza la hipótesis nula \( H_0: ρ = 0 \). Existe evidencia suficiente para concluir que la correlación es diferente de cero.")
else:
    st.write("**Resultado:** No se rechaza la hipótesis nula \( H_0: ρ = 0 \). No existe evidencia suficiente para concluir que la correlación es diferente de cero.")
