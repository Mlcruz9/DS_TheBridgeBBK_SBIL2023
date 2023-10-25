import streamlit as st
import pandas as pd
from PIL import Image
# from functions import home, datos, cargar_datos, menu_filtros
#st.beta_expander ahora es expander
# Este es mi script

st.set_page_config(page_title='Cargatron', layout='wide', page_icon=':battery:')
data = pd.read_csv('data/red_recarga_acceso_publico_2021.csv', sep = ';')
data


uploaded_file = st.file_uploader("Sube un archivo .csv", type= ['.csv'])

st.write('Hola mundo')

# st.balloons()