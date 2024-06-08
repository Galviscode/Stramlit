import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
# Set the page title and header
st.title("Simulador CESDE Bello")

df = pd.read_csv('static/datasets/cesde.csv')

gruposU = sorted(df['GRUPO'].unique())
nivelesU = sorted(df['NIVEL'].unique())
jornadasU = sorted(df['JORNADA'].unique())
momentosU = sorted(df['MOMENTO'].unique())

# -----------------------------------------------------------------------------------
def filtro1():    
    col1, col2 = st.columns(2)
    with col1:
        grupo = st.selectbox("Grupo", gruposU)
    with col2:
        momento = st.selectbox("Momento", momentosU)
    resultado = df[(df['GRUPO'] == grupo) & (df['MOMENTO'] == momento)]
   
    resultado = resultado.reset_index(drop=True) 
    # Grafico de barras
    estudiante = resultado['NOMBRE']
    fig = go.Figure(data=[
        go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
        go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
        go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
    ])   
    fig.update_layout(barmode='group')
    st.plotly_chart(fig, use_container_width=True)
    # Tabla
    st.table(resultado[["NOMBRE", "CONOCIMIENTO", "DESEMPEÑO", "PRODUCTO"]])
    
# -----------------------------------------------------------------------------------
def filtro2():
    col1, col2, col3 = st.columns(3)
    with col1:
        grupo = st.selectbox("Grupo", gruposU)
    with col2:
        nombres = df[df['GRUPO'] == grupo]
        nombre = st.selectbox("Estudiante", nombres["NOMBRE"])
    with col3:
        momentosU.append("Todos")
        momento = st.selectbox("Momento", momentosU)   

    if momento == "Todos":
        resultado = df[(df['GRUPO'] == grupo) & (df['NOMBRE'] == nombre)]
        # Grafico de barras
        momentos = sorted(df['MOMENTO'].unique())
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=momentos, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=momentos, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=momentos, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado = resultado.reset_index(drop=True) 
        m1 = resultado.loc[0, ['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']]
        m2 = resultado.loc[1, ['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']]
        m3 = resultado.loc[2, ['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']]
        tm = pd.Series([m1.mean(), m2.mean(), m3.mean()])       
        st.subheader("Promedio")
        st.subheader(round(tm.mean(), 1)) 
    else:   
        resultado = df[(df['GRUPO'] == grupo) & (df['MOMENTO'] == momento) & (df['NOMBRE'] == nombre)]
        # Grafico de barras
        estudiante = resultado['NOMBRE']
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=estudiante, y=resultado['CONOCIMIENTO']),
            go.Bar(name='DESEMPEÑO', x=estudiante, y=resultado['DESEMPEÑO']),
            go.Bar(name='PRODUCTO', x=estudiante, y=resultado['PRODUCTO'])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)

        resultado = resultado.reset_index(drop=True) 
        conocimiento = resultado.loc[0, ['CONOCIMIENTO', 'DESEMPEÑO', 'PRODUCTO']]
        st.subheader("Promedio")
        st.subheader(round(conocimiento.mean(), 1)) 

# -----------------------------------------------------------------------------------
def filtro_niveles_jornadas():
    col1, col2 = st.columns(2)
    with col1:
        nivel = st.selectbox("Nivel", nivelesU)
    with col2:
        jornada = st.selectbox("Jornada", jornadasU)
    
    resultado = df[(df['NIVEL'] == nivel) & (df['JORNADA'] == jornada)]
    resultado = resultado.reset_index(drop=True)
    
    if not resultado.empty:
        promedio_conocimiento = resultado['CONOCIMIENTO'].mean()
        promedio_desempeño = resultado['DESEMPEÑO'].mean()
        promedio_producto = resultado['PRODUCTO'].mean()
        
        st.subheader(f"Promedios para Nivel {nivel} y Jornada {jornada}")
        st.write(f"Promedio Conocimiento: {promedio_conocimiento:.2f}")
        st.write(f"Promedio Desempeño: {promedio_desempeño:.2f}")
        st.write(f"Promedio Producto: {promedio_producto:.2f}")
        
        # Gráfico de barras
        fig = go.Figure(data=[
            go.Bar(name='CONOCIMIENTO', x=['Promedio'], y=[promedio_conocimiento]),
            go.Bar(name='DESEMPEÑO', x=['Promedio'], y=[promedio_desempeño]),
            go.Bar(name='PRODUCTO', x=['Promedio'], y=[promedio_producto])
        ])   
        fig.update_layout(barmode='group')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No hay datos para los filtros seleccionados.")

# -----------------------------------------------------------------------------------
filtros = [
    "Notas por grupo",
    "Notas por estudiante",
    "Promedios por nivel y jornada"
]

filtro = st.selectbox("Filtros", filtros)

if filtro:
    filtro_index = filtros.index(filtro)

    if filtro_index == 0:
        filtro1()
    elif filtro_index == 1:
        filtro2()
    elif filtro_index == 2:
        filtro_niveles_jornadas()
