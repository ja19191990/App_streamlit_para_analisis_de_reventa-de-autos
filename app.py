import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown('''
            <style>
            .stForm {
            background-color: #0000000
            }
            </style>
''', unsafe_allow_html=True)

st.header('Vehicles advertisement')
st.write('Selecciona el gráfico deseado')

car_data = pd.read_csv('datasets/cars_us.csv')
hist_check_price = st.checkbox('Desplegar histograma de precios')
if hist_check_price:
    st.write('Histograma del precio de vehículos')
    st.write('Mayor frecuencia de precios entre 2 mil y 9 mil USD')
    # crear histograma
    fig_p = px.histogram(car_data, x='price')
    # mostrar gráfico de plotly interactivo
    st.plotly_chart(fig_p, use_container_width=True)

hist_check_year = st.checkbox('Desplegar histograma de modelos vehículares')
if hist_check_year:
    st.write('Histograma del modelo de los vehículos')
    st.write('Desde el 2000 incrementaron los vehículos. \nEn el 2013 se alcanzó el valor máximo. Posteriormente se observa un descenso.')
    # crear histograma
    fig_y = px.histogram(car_data, x='model_year')
    # mostrar gráfico de plotly interactivo
    st.plotly_chart(fig_y, use_container_width=True)

hist_check_condition = st.checkbox('Desplegar histograma enfocado en la condición de los vehículos')
if hist_check_condition:
    st.write('Histograma de la condición de los vehículos')
    st.write('La mayoría de los vehículos están en una condición Buena o Excelente. \nSon mínimos los carros nuevos y reacondicionados.')
    # crear histograma
    fig_c = px.histogram(car_data, x='condition')
    # mostrar gráfico de plotly interactivo
    st.plotly_chart(fig_c, use_container_width=True)

# construir diagram de dispersión
scatter_check = st.checkbox('Desplegar diagrama de dispersión Precio vs Modelo')
if scatter_check:
    st.write('Dispersión del precio contra modelo vehícular')
    st.write('La mayoría de los vehículos entre los años 2000 y 2020 valen menos de 100,000 USD')
    # crear dispersión
    fig_s = px.scatter(car_data, y='price', x='model_year')
    # mostrar dispersión plotly interactivo
    st.plotly_chart(fig_s, use_container_width=True)