
import streamlit as st
import matplotlib.pyplot as plt

# Set the page title and header
st.title("Proyecto Integrador")
st.header("Bienvenido a nuestro Proyecto Integrador BoomMusic")

# Hero Section with image and project description
st.image("https://i.postimg.cc/q7VNRHRJ/logo-proyecto.png", width=600)
st.write("Este proyecto integrador busca mostrar estadisticas de la industria musical, con una amplia base de datos .")

# Project Overview
st.subheader("Descripcion de los proyectos")
st.write("- Proyecto 1: ")
st.write("- Proyecto 2, El Simulador CESDE Bello es una herramienta interactiva desarrollada con Streamlit para facilitar el análisis y visualización de datos académicos del CESDE Bello. Permite a los usuarios filtrar y explorar las calificaciones de los estudiantes a través de diversas dimensiones, incluyendo grupos, niveles y jornadas.")
st.write("- Punto 3: Descripción detallada del punto 3 del proyecto.")


# Call to Action
st.subheader("¡Toma Acción!")
st.write("**Visite nuestro sitio web:** [Enlace al sitio web del proyecto](https://example.com)")
st.write("**Contáctenos:** [Enlace al correo electrónico de contacto](mailto:info@example.com)")

# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("**Miembros del equipo:**")
st.write("- Nombre 1: Cargo en el equipo.")
st.write("- Nombre 2: Cargo en el equipo.")
st.write("- Nombre 3: Cargo en el equipo.")
st.write("**Información de contacto:**")
st.write("Correo electrónico: [Enlace al correo electrónico de contacto](mailto:info@example.com)")