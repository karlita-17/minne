import streamlit as st

# Página 1: Los Galácticos
def pagina_los_galacticos():
    st.title("Los Galácticos")
    st.write("""
        Los Galácticos son una agrupación musical destacada por su estilo único y energía inigualable.
        """)
    st.image("los galacticos-copia.png", caption="lo mejor de chile")

# Página 2: Jere Klein
def pagina_jere_klein():
    st.header("Jere Klein")
    st.write("""
    Jeremías Tobar, conocido artísticamente como Jere Klein, es un cantante y compositor chileno destacado en la música urbana.
    """)
    st.video("https://www.youtube.com/watch?v=Bw-pZjg7wZg&list=RDBw-pZjg7wZg&start_radio=1")  # Video oficial UNA EN UN MILLON

# Página 3: Lucky Brown
def pagina_lucky_brown():
    st.header("Lucky Brown")
    st.write("""
    Lucky Brown es un destacado artista chileno reconocido por sus colaboraciones y estilo urbano innovador.
    """)
    st.image("lucky.jpeg", caption="Lucky Brown")

# Página 4: Paloma Mami
def pagina_paloma_mami():
    st.header("Paloma Mami")
    st.write("""
    Paloma Mami es una famosa cantante chileno-estadounidense reconocida por su talento y música popular.
    """)
    st.video("https://www.youtube.com/watch?v=ltYUH6fEYdE&list=RDltYUH6fEYdE&start_radio=1")  # Video de ejemplo

# Página "Quiénes Somos" con información ficticia
def pagina_quienes_somos():
    st.header("Quiénes Somos")
    st.write("""
    Hola, soy Sofía, creadora de este sitio web dedicado a la música urbana chilena.
    Esta página contiene información ficticia para proteger la privacidad. 
    """)
    st.image("https://images.unsplash.com/photo-1529156069898-49953e39b3ac", caption="Sofía, creadora del sitio")

# Diccionario con las páginas
paginas = {
    "Los Galácticos": pagina_los_galacticos,
    "Jere Klein": pagina_jere_klein,
    "Lucky Brown": pagina_lucky_brown,
    "Paloma Mami": pagina_paloma_mami,
    "Quiénes Somos": pagina_quienes_somos
}

# Barra lateral para navegar
st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Selecciona una página", list(paginas.keys()))

# Mostrar página seleccionada
pagina_seleccionada = paginas[opcion]
pagina_seleccionada()

