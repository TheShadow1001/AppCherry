import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="OptiJuegos",
    page_icon="🎮",
    layout="centered",
)

# Estilo CSS personalizado para replicar la estética
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: white;
        }
        .title {
            font-size: 50px;
            text-align: center;
            font-weight: bold;
            color: #00ffcc;
        }
        .subtitle {
            font-size: 24px;
            text-align: center;
            color: white;
        }
        .button-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 40px;
        }
        .stButton>button {
            background-color: #00ffcc;
            color: black;
            padding: 10px 24px;
            font-size: 18px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<div class="title">OptiJuegos</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">¡Bienvenido a la nueva era del gaming!</div>', unsafe_allow_html=True)

# Contenedor de botones
st.markdown('<div class="button-container">', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.button("JUEGO 1")
    st.button("JUEGO 2")
with col2:
    st.button("JUEGO 3")
    st.button("JUEGO 4")
st.markdown('</div>', unsafe_allow_html=True)
