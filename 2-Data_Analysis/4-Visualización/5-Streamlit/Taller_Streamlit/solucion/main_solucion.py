import streamlit as st
import pandas as pd
from PIL import Image
from functions_solucion import home, datos, cargar_datos, menu_filtros

# Este es mi script

st.set_page_config(page_title='Cargatron', layout='wide', page_icon=':battery:')

menu = st.sidebar.selectbox(
    "Seleccione una opción del menu",
    ('Home', 'Datos', 'Filtros')
)

uploaded_file = st.sidebar.file_uploader("Carga tus propios datos", type=['csv'])

if menu == 'Home':
    home()
elif menu == 'Datos':
    df = cargar_datos()
    datos(df, 11)
elif menu == 'Filtros':
    menu_filtros()



#st.balloons()

