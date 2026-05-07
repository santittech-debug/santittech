import streamlit as st
import pandas as pd


ruta_zni = 'https://github.com/juliandariogiraldoocampo/analisis_taltech/raw/refs/heads/main/explorador/ZNI.csv'

df = pd.read_csv(ruta_zni)



st.title('Estado de la presentacion del servicio de energia')
st.header('Zonas no interconectadas (ZNI)')
st.subheader('conjunto de datos')

st.dataframe(df)