import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
# Set the page title and header
st.title("Datos de llamadas")

df = pd.read_csv('static\datasets\llamadas.csv', sep=';', encoding='latin-1' )

localidades = sorted(df['LOCALIDAD'].unique())
generos = sorted(df['GENERO'].unique())

# Definir el filtro
def filtro1():
    col1, col2 = st.columns(2)
    with col1:
        localidad = st.selectbox("Localidad", localidades)
    
    # Filtrar el dataframe según la selección de localidad
    resultado = df[df['LOCALIDAD'] == localidad]
    resultado = resultado.reset_index(drop=True)
    
    # Agrupar por LOCALIDAD y GENERO y contar el número de incidentes
    accidentes_por_localidad_genero = resultado.groupby(['LOCALIDAD', 'GENERO']).size().reset_index(name='Cantidad de Accidentes')
    
    # Crear el gráfico de barras
    fig = go.Figure()
    for genero in generos:
        data = accidentes_por_localidad_genero[accidentes_por_localidad_genero['GENERO'] == genero]
        fig.add_trace(go.Bar(
            x=data['LOCALIDAD'],
            y=data['Cantidad de Accidentes'],
            name=genero
        ))
    
    fig.update_layout(
        title="Cantidad de Accidentes por Localidad y Género",
        xaxis_title="Localidad",
        yaxis_title="Cantidad de Accidentes",
        barmode='group'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar la tabla
    st.table(accidentes_por_localidad_genero)

# Llamar a la función de filtro
filtro1()
