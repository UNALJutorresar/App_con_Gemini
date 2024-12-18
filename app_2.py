# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pDHLEpb9twY3UIBvujQGBGIog7lAj2HW
"""

import streamlit as st
import re

# Título de la app
st.title('Verificador de formato')

# Autor de la app
st.write('Esta app fue elaborada por Juan Camilo Torres Arboleda.')

# Descripción de la app
st.write('''
            Ingresa tus datos en los campos y presiona "Validar" para
            verificar si están en el formato correcto.
        ''')

def validar_nombre(nombre):
    patron = r"^[A-Z][a-zA-Z]+$"
    return bool(re.match(patron, nombre))

def validar_email(email):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, email))

def validar_telefono(telefono):
    patron = r"^\+\d{1,3}\s\d{10}$"
    return bool(re.match(patron, telefono))

def validar_fecha(fecha):
    patron = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(patron, fecha):
        return False

    anio, mes, dia = map(int, fecha.split('-'))
    if not 1 <= mes <= 12:
        return False
    if dia < 1 or dia > 31:
        return False
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    if mes == 2 and dia >= 29:
        return False

    return True

st.title("Formulario de Validación")

nombre = st.text_input("Ingrese su nombre completo")
email = st.text_input("Ingrese su correo electrónico")
telefono = st.text_input("Ingrese su número de teléfono (+XX XXXXXXXXXX)")
fecha = st.text_input("Ingrese una fecha (AAAA-MM-DD)")

if st.button("Validar"):
    if validar_nombre(nombre):
        st.success("Nombre válido.")
    else:
        st.error("Nombre inválido. Debe comenzar con mayúscula y solo contener letras.")

    if validar_email(email):
        st.success("Correo electrónico válido.")
    else:
        st.error("Correo electrónico inválido.")

    if validar_telefono(telefono):
        st.success("Número de teléfono válido.")
    else:
        st.error("Número de teléfono inválido.")

    if validar_fecha(fecha):
        st.success("Fecha válida.")
    else:
        st.error("Fecha inválida. Use el formato AAAA-MM-DD y revise valores.")