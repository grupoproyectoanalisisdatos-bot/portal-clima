import streamlit as st

# Configuración estética
st.set_page_config(page_title="Portal Agrícola Colombiano", layout="centered")

# CSS personalizado para que los botones parezcan tarjetas
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        height: 150px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid #4CAF50;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #4CAF50;
        color: white;
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌱 Sistema Inteligente de Gestión Agrícola")
st.subheader("Seleccione el módulo que desea consultar:")

st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Análisis de Datos")
    st.write("Explora la relación histórica entre clima y cosechas (IDEAM/Agronet).")
    # Enlace directo a tu primera app
    st.link_button("Abrir Dashboard de Clima", "https://app-mi-proyecto-clima.streamlit.app/")

with col2:
    st.markdown("### 🔮 Predicción")
    st.write("Accede al modelo de Machine Learning para proyecciones de rendimiento.")
    # Enlace directo a tu segunda app
    st.link_button("Abrir Modelo Predictivo", "https://appmodelopredictivoclima.streamlit.app/")

st.write("---")
st.caption("Centralización de herramientas para la toma de decisiones agrícolas en Colombia.")
