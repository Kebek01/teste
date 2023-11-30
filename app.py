import streamlit as st
st.title('calculadora')

num1= st.number_input('digite o primeiro numero ')
num2= st.number_input('digite o segundo numero ')
a2=num1 - num2
a3=num1 * num2
a4=num1 / num2

if st.button('calcular'): 
    st. text(f'resultado:\n soma: {num1 + num2}\n subtração: {a2} \n multiplicação: {a3}\n divisão: {a4}')

