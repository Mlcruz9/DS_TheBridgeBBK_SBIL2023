import streamlit as st
import pandas as pd
from PIL import Image


def cargar_datos():
    path_csv = 'data/red_recarga_acceso_publico_2021.csv'
    df = pd.read_csv(path_csv, sep=';')

    # uploaded_file = st.file_uploader("Carga tus propios datos", type=['csv'])
    return df


def home():
    st.title('Cargatron')
    image = Image.open('img/puntos-recarga-madrid.jpg')

    st.image(image, caption='Coche cargando')

    df = cargar_datos()

    with st.expander('¿Quieres saber más?'):
        st.write('Ante el problema climático al que nos enfrentamos, el coche eléctrico se plantea como una solución posible. Queremos facilitarte que encuentres tu puesto de carga más cercano')

    with st.echo():
        st.dataframe(df)
    

def datos(df, zoom):


    df.rename(columns={"longitud": "lon", "latidtud": "lat"}, inplace=True)

    st.map(df[['lon','lat']], zoom=zoom)

    st.bar_chart(df.groupby(['DISTRITO'])[['Nº CARGADORES']].sum())

    st.bar_chart(df.groupby(['OPERADOR'])[['Nº CARGADORES']].sum())

def menu_filtros():
    menu = st.sidebar.selectbox(
    "Seleccione una opción de filtro",
    ('Distrito', 'Operador'))

    df = cargar_datos()
    if menu == "Distrito":
        datos(df, 13)
    else:
        n_cargadores = st.sidebar.select_slider(
        'Filtra por número de cargadores',
        options=list(range(df['Nº CARGADORES'].min(), df['Nº CARGADORES'].max()+1)))
        agree_c = st.sidebar.checkbox('Filtrar por cargadores')
        if agree_c:
            df_filtered = filtrar(n_cargadores)
            datos(df_filtered, 11)
            st.warning('This is a warning')

def filtrar(filtro):
    df = cargar_datos()
    df_filtered = df[df['Nº CARGADORES']==filtro]
    return df_filtered

    