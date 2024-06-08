import streamlit as st
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Proyecto Integrador BoomMusic", layout="wide")

# Título y encabezado
st.title("Proyecto Integrador BoomMusic")
st.header("Bienvenido a nuestro Proyecto Integrador")

# Sección Hero con imagen y descripción del proyecto
st.image("https://i.postimg.cc/q7VNRHRJ/logo-proyecto.png", width=600)
st.markdown("""
**BoomMusic** es un proyecto integrador que busca mostrar estadísticas de la industria musical, utilizando una amplia base de datos. 
La plataforma proporciona herramientas interactivas para explorar y analizar datos musicales de manera dinámica.
""")

# Resumen del proyecto
st.subheader("Descripción de los Proyectos")
st.markdown("""
### Proyecto 1: Exploración de Datos Musicales
Este proyecto integrador es una aplicación interactiva desarrollada con Streamlit y Plotly. Está diseñada para explorar y analizar datos musicales de una manera dinámica e intuitiva. 
Los usuarios pueden seleccionar géneros, artistas y álbumes específicos para visualizar información detallada sobre sus contenidos y popularidades, proporcionando una herramienta poderosa para la visualización y el análisis de datos en el ámbito musical.

### Proyecto 2: Simulador CESDE Bello
El Simulador CESDE Bello es una herramienta interactiva desarrollada con Streamlit para facilitar el análisis y la visualización de datos académicos del CESDE Bello. 
Permite a los usuarios filtrar y explorar las calificaciones de los estudiantes a través de diversas dimensiones, incluyendo grupos, niveles y jornadas.

### Proyecto 3: Análisis de Datos de Llamadas de Emergencias
Este proyecto es una aplicación interactiva desarrollada con Streamlit, destinada a visualizar y analizar datos de llamadas de emergencias (123) para marzo de 2024. 
La aplicación permite a los usuarios explorar la información de manera dinámica, filtrando los datos por localidad, género y edad para obtener insights específicos sobre los incidentes registrados.
""")

# Sección de equipo y contacto
st.subheader("Equipo y Contacto")
st.markdown("""
**Miembros del equipo:**
- Julian David Marín Iglesias
- Andrés Galvis Atehortúa
- Johan Rodríguez Pérez

Para más información, contáctanos a través de [correo@example.com](mailto:correo@example.com).
""")

# Espacio en blanco para una mejor separación visual
st.markdown("###")
st.markdown("###")

# Footer
st.markdown("""
---
*Desarrollado por el equipo de BoomMusic - 2024*
""")
