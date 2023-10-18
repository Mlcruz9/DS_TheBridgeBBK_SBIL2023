from functions import *
from variables import *

name_start = 'j'
name_start = name_start.upper()
counter = 0
offset = 0
respuesta = peticion(pub_key= pub_key, priv_key= priv_key, name_start=name_start, offset=offset)
total = respuesta['data']['total']
df_concat = []

while counter < total:
    respuesta = peticion(pub_key= pub_key, priv_key= priv_key, name_start=name_start, offset=offset)
    df = character_df(res=respuesta)
    df_concat.append(df)
    counter += df.shape[0]
    offset += 100

df_concat = pd.concat(df_concat)
df_concat.reset_index(inplace=True, drop= True)

df_concat.to_csv('data/charactersby' + name_start + '.csv')



