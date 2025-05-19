import streamlit as st

# --------- Funciones helper ---------
def load_projects():
    return [
        {
            "title": "Web Corporativa",
            "desc": "Diseño y desarrollo de sitio web responsive para empresa de tecnología.",
            "img": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=600&q=80",
            "url": "https://example.com/proyecto1"
        },
        {
            "title": "App Móvil",
            "desc": "App híbrida multiplataforma con funcionalidades offline y notificaciones.",
            "img": "https://images.unsplash.com/photo-1506765515384-028b60a970df?auto=format&fit=crop&w=600&q=80",
            "url": "https://example.com/proyecto2"
        },
        {
            "title": "E-commerce Moderno",
            "desc": "Plataforma de comercio electrónico con carrito y pasarela de pago integrada.",
            "img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=600&q=80",
            "url": "https://example.com/proyecto3"
        }
    ]

def show_projects(projects):
    st.markdown("## 🚀 Proyectos Destacados")
    cols = st.columns(3)
    for i, proj in enumerate(projects):
        with cols[i]:
            st.image(proj["img"], use_column_width=True, caption=proj["title"])
            st.markdown(f"**{proj['title']}**")
            st.write(proj["desc"])
            st.markdown(f"[Ver más]({proj['url']})")

# --------- Layout y configuración ---------
st.set_page_config(
    page_title="Panita Dev - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------- Barra lateral con navegación ---------
with st.sidebar:
    st.title("👋 Hola, soy Panita Dev")
    st.write("Desarrollador web ultra profesional con estilo moderno y accesible.")
    page = st.radio("Navegación", ["Inicio", "Proyectos", "Sobre mí", "Contacto"])
    st.markdown("---")
    st.write("🌙 Modo Oscuro/Claro")
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    if st.button("Toggle Tema"):
        st.session_state.dark_mode = not st.session_state.dark_mode

if st.session_state.dark_mode:
    st.markdown(
        """
        <style>
        .main {
            background-color: #121212;
            color: #eee;
        }
        .stButton>button {
            background-color: #333;
            color: #eee;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
        .main {
            background-color: #fff;
            color: #111;
        }
        .stButton>button {
            background-color: #eee;
            color: #111;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --------- Contenido según selección ---------
if page == "Inicio":
    st.title("Hola, soy Panita Dev 👨‍💻")
    st.write("""
    Bienvenido a mi portfolio online. Aquí comparto mis proyectos, mi experiencia y cómo contactarme.
    """)
    st.image("https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=800&q=80", use_column_width=True)

elif page == "Proyectos":
    projects = load_projects()
    show_projects(projects)

elif page == "Sobre mí":
    st.header("Sobre mí")
    st.write("""
    Soy un desarrollador apasionado por crear experiencias web de alta calidad. Me especializo en frontend y backend, siempre buscando nuevas tecnologías y buenas prácticas para mejorar mis proyectos.
    """)
    st.write("Me encanta compartir conocimiento y aprender día a día. 🚀")

elif page == "Contacto":
    st.header("Contacto 📬")
    with st.form("contact_form"):
        nombre = st.text_input("Nombre completo", max_chars=50)
        email = st.text_input("Correo electrónico")
        mensaje = st.text_area("Mensaje", height=150)
        enviar = st.form_submit_button("Enviar")
        if enviar:
            if len(nombre) < 3:
                st.error("El nombre debe tener al menos 3 caracteres.")
            elif "@" not in email or "." not in email:
                st.error("Por favor, ingresa un correo válido.")
            elif len(mensaje) < 10:
                st.error("El mensaje debe tener al menos 10 caracteres.")
            else:
                st.success("¡Mensaje enviado con éxito! (Simulado)")

# --------- Footer simple ---------
st.markdown("---")
st.markdown("© 2025 Panita Dev. Todos los derechos reservados.")
