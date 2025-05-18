import streamlit as st

st.title("AppCherry")
st.subheader("Welcome To AppCherry")
st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhao2edUau_Ywxfw60-Ug0-0w6MaHJ9EkYvfw4QyN4DTl-3lnzBhE7Awl5wXaELy6spSN4aoSQLVi95fFDcSNeT3RN8QR5NmsuGDyXj7PsmoPGFP1_W98hBvKyAJjFp2_83KhpRbpPVao_wINUWTn_YnsoWRkAxQM9GN3PMgJk08NHpfMmyTeUYokQurFo/s600/AppCherry2.png")
st.info("WELCOME TO PROJECT")
st.write("AppCherry es una plataforma web, dónde los vendedores y compradores pueden comprar, vender Etc.")
st.write("Con esta plataforma tendrás mucha comodidad a la hora de buscar o vender productos.")
st.write("Cabe aclarar que esta página fue hecho por @WikiDev, talvez no sea alguien conocido.")
st.write("Esta página es una beta v1.0, así que es posible la precencia de algún error.")
st.write("Si tiene algúna duda o simplemente quieres dar algún error ocurrido puedes contactarme, por @WikiDeveloper@gmail.com")
st.subheader("¡Agradezco! su paciencia, Estaré al tanto del proyecto lo mejor pósible por su comodidad.")

st.text_input("¿Qué Opinás Del Proyecto?")
st.button("Envíar Opinión")

st.header("Registrarse")


st.subheader("Tendrás que registrarte para procceder!")

st.write("Si no te registras no podrás usar la app.")
st.write("Solo Tendrás que poner un nombre, una contraseña osea crear una, y un correo eléctronico.")

usuario = st.text_input("Nombre_Usuario")
correo = st.text_input("Corréo eléctronico")
contrasena = st.text_input("contraseña")
registrar = st.button("Registrarme a AppCherry")

st.subheader("@WikiDev")
