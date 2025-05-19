import streamlit as st

st.title("AppCherry")
st.image("C:\Users\IK\Desktop\AppCherry.png", caption="AppCherry", width=300)
st.subheader("Welcome To AppCherry")
st.write("AppCherry es una plataforma web, dónde los vendedores y compradores puedes elegir como una opción elegíble.")
st.write("Con esta plataforma tendrás mucha comodidad a la hora de buscar o vender productots.")
st.write("Cabe aclarar que esta página fue hecho por @WikiDev, talvez no sea alguien conocido.")
st.write("Esta página es una beta v1.0, así que es posible la precencia de algún error.")
st.write("Si tiene algúna duda o simplemente quieres dar algún error ocurrido puedes contactarme, por @WikiDeveloper@gmail.com")
st.subheader("¡Agradezco! su paciencia, Estaré al tanto del proyecto lo mejor pósible por su comodidad.")


st.subheader("Tendrás que registrarte para procceder!")

st.write("Si no te registras no podrás usar la app.")
st.write("Solo Tendrás que poner un nombre, una contraseña osea crear una, y un correo eléctronico.")

if "registrado" not in st.session_state:
    st.session_state.registrado = False

if not st.seassion_state.registrado:
    st.subheader("Registro")
    nombre = st.text_input("Nombre de usuario")
    contraseña = st.text_input("Contraseña", type="password")
    correo = st.text_input("Correo eléctronico")

    if st.button("Registrarse"):
        if nombre and contraseña and correo:
            st.session_state.registrado = True
            st.success("Registro exitoso!")
        else:
            st.error("Por favor, completa todos los campos.")
         

st.subheader("Descripción")

st.write("Esta página fué hecha 100% con streamlit, y la página está siendo mantenida y actualizada por mí.")
st.write("La página Está en desarrollo, así que ahora no se podrá públicar ni comprar nada, pero dentro de 2 días será posible.")
st.write("La página Es (BETA), así que es común algún error.")

st.text_input("¿Cómo Debería Mejorarla?")

Acepto = st.button("Acepto")

if Acepto:
    if Acepto:
        st.success("Gracias por su opinión")
    else:
        st.warning("Diga algúna opinión sobre como mejorar la página.")

st.info("Puedes visitar Mi página de juegos:)")

st.write("https://wikiproyects.blogspot.com/2025/05/blog-post.html")
