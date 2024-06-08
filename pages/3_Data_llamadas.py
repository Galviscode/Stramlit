import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
# Set the page title and header
st.title("Datos de llamadas")

df = pd.read_csv('static/datasets/llamadas_123_marzo2024.csv', sep=';', encoding='latin-1')

# Obtener las localidades y géneros únicos
localidades = sorted(df['LOCALIDAD'].unique())
generos = sorted(df['GENERO'].unique())
generos.append("Todos")  # Agregar la opción "Todos" al filtro de género

# Definir el filtro de accidentes por localidad, género y edad
def filtro1():
    col1, col2, col3 = st.columns(3)
    with col1:
        localidad = st.selectbox("Localidad", localidades)
    
    with col2:
        edad = st.radio("Selecciona un rango de edad", ["Menores de 18 años", "Mayores de 18 años"])
    
    with col3:
        genero = st.selectbox("Selecciona un género", generos)
    
    # Filtrar el dataframe según la selección de localidad, edad y género
    resultado = df[df['LOCALIDAD'] == localidad]
    if edad == "Menores de 18 años":
        resultado = resultado[resultado['EDAD'] < 18]
    else:
        resultado = resultado[resultado['EDAD'] >= 18]
    if genero != "Todos":
        resultado = resultado[resultado['GENERO'] == genero]
    resultado = resultado.reset_index(drop=True)
    
    # Agrupar por LOCALIDAD, GÉNERO y EDAD y contar el número de incidentes
    accidentes_por_localidad_genero_edad = resultado.groupby(['LOCALIDAD', 'GENERO', 'EDAD']).size().reset_index(name='Cantidad de Accidentes')
    
    # Crear el gráfico de barras
    fig = px.bar(accidentes_por_localidad_genero_edad, x='LOCALIDAD', y='Cantidad de Accidentes', color='GENERO',
                 title=f"Cantidad de Accidentes {edad} por Localidad y Género ({'Todos' if genero == 'Todos' else genero})",
                 barmode='group')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Mostrar la tabla de incidentes
    st.subheader(f"Tabla de Accidentes {edad} por Localidad y Género ({'Todos' if genero == 'Todos' else genero})")
    st.table(accidentes_por_localidad_genero_edad)

# Llamar a la función de filtro
filtro1()

