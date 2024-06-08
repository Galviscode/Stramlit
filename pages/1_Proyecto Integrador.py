import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el archivo CSV
df = pd.read_csv('static/datasets/musica.csv')

# Obtener géneros únicos
generos = df['track_genre'].unique()

# Filtro de género
genero_seleccionado = st.selectbox("Selecciona un género:", generos)

# Filtrar el DataFrame por el género seleccionado
df_genero = df[df['track_genre'] == genero_seleccionado]

# Obtener artistas únicos del género seleccionado
artistas_genero = df_genero['artists'].unique()

# Filtro de artista
artista_seleccionado = st.selectbox("Selecciona un artista:", artistas_genero)

# Filtrar el DataFrame por el artista seleccionado
df_artista = df_genero[df_genero['artists'] == artista_seleccionado]

# Obtener álbumes únicos del artista seleccionado
albumes_artista = df_artista['album_name'].unique()

# Filtro de álbum
album_seleccionado = st.selectbox("Selecciona un álbum:", albumes_artista)

# Filtrar el DataFrame por el álbum seleccionado
df_album = df_artista[df_artista['album_name'] == album_seleccionado]

# Mostrar tabla con el contenido del álbum seleccionado
st.write(f"Contenido del álbum '{album_seleccionado}' de {artista_seleccionado}:")
st.write(df_album)

# Obtener la popularidad del álbum, artista y género seleccionados
popularidad_album = df_album['popularity'].iloc[0]  # Tomamos la popularidad del primer registro del álbum
popularidad_artista = df_artista['popularity'].iloc[0]  # Tomamos la popularidad del primer registro del artista
popularidad_genero = df_genero['popularity'].mean()  # Calculamos la popularidad promedio del género

# Crear un DataFrame para el gráfico
data = {
    'Métrica': ['Popularidad del Álbum', 'Popularidad del Artista', 'Popularidad Promedio del Género'],
    'Popularidad': [popularidad_album, popularidad_artista, popularidad_genero]
}
df_popularidad = pd.DataFrame(data)

# Crear el gráfico de barras
fig = px.bar(df_popularidad, x='Métrica', y='Popularidad', color='Métrica', title='Comparación de Popularidades')
fig.update_layout(xaxis_title='Métrica', yaxis_title='Popularidad')
st.plotly_chart(fig, use_container_width=True)
