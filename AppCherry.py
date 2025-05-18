import streamlit as st

st.title("AppCherry Chat")

# Crear dos columnas: una para el chat y otra para los botones
col1, col2 = st.columns([4, 1])

with col1:
    mensaje = st.text_input("Escribe tu mensaje aquí...")

with col2:
    enviar = st.button("Enviar")

# Mostrar el mensaje enviado (simulación de chat)
if enviar and mensaje:
    st.success(f"Tú: {mensaje}")
