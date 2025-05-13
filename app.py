import streamlit as st

# Diccionario con masa molar de 5 solutos (g/mol)
solutos = {
    "NaCl (Cloruro de sodio)": 58.44,
    "KCl (Cloruro de potasio)": 74.55,
    "C6H12O6 (Glucosa)": 180.16,
    "H2SO4 (Ácido sulfúrico)": 98.08,
    "CaCl2 (Cloruro de calcio)": 110.98
}

st.title("Calculadora de Concentración Molar")
st.write("Selecciona un soluto e ingresa la masa en gramos para calcular la concentración molar en una solución de 1 litro.")

# Selección del soluto
soluto = st.selectbox("Selecciona un soluto", list(solutos.keys()))

# Entrada de masa
masa = st.number_input("Ingresa la masa del soluto (en gramos)", min_value=0.0, step=0.1)

# Botón para verificar y calcular
if st.button("Calcular concentración molar"):
    masa_molar = solutos[soluto]
    moles = masa / masa_molar
    concentracion_molar = moles / 1  # porque es por 1 litro

    st.success(f"La concentración molar de {soluto} es **{concentracion_molar:.4f} mol/L**")
