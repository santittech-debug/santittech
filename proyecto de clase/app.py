import streamlit as st
import pandas as pd

st.image('imagenes\Captura de pantalla 2026-05-07 205140.png', width=900)

st.header('Operaciones de importacion ')
st.text('Conjunto de Datos')

# carga de datos
ruta= 'data/operaciones mde.csv' 

df= pd.read_csv(ruta)

## analisis de los datos

filas = df.shape[0]
columnas = df.shape[1]

## visualización 

col1,col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader('filas')
        st.text(filas)

with col2:
    with st.container(border=True):
        st.subheader('columna')
        st.text(columnas)

##otra forma de mostrar los indicadores
#col3,col4 = st.columns(2)
#with col3:
    #st.metric('numero de filas', filas, border=True)

#with col4:
    #st.metric('numero de columnas', columnas, border=True)

cantidad_clientes = df['Cliente'].nunique()
cantidad_operaciones = df['FileID'].count()

# =========================
# VISUALIZACION
# =========================

col5, col6 = st.columns(2)

with col5:
    with st.container(border=True):
        st.subheader('Cantidad de clientes')
        st.metric(label='Cliente', value=cantidad_clientes)

with col6:
    with st.container(border=True):
        st.subheader('Cantidad de operaciones')
        st.metric(label='FileID', value=cantidad_operaciones)

st.dataframe(df)

df.describe(include='object')
st.write(df.describe(include='object'))

print('Hola Mundo')

