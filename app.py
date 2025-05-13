import streamlit as st

# Diccionario con masa molar de 5 solutos (g/mol)
solutos = {
    "NaCl (Cloruro de sodio)": 58.44,
    "KCl (Cloruro de potasio)": 74.55,
    "C6H12O6 (Glucosa)": 180.16,
    "H2SO4 (Ácido sulfúrico)": 98.08,
    "CaCl2 (Cloruro de calcio)": 110.98
}

st.title("¿Puedes calcular la concentración molar correctamente?")

st.write("""
Selecciona un soluto, ingresa una masa en gramos y escribe tu respuesta estimada de concentración molar (mol/L) para una solución de **1 litro**.
""")

# Selección del soluto
soluto = st.selectbox("Selecciona un soluto:", list(solutos.keys()))
peso_molar = solutos[soluto]

st.info(f"Peso molar de {soluto}: **{peso_molar} g/mol**")

# Ingreso de la masa
masa = st.number_input("Ingresa la masa del soluto (en gramos):", min_value=0.0, step=0.1)

# Ingreso de la respuesta del usuario
respuesta_usuario = st.number_input("¿Cuál es tu respuesta para la concentración molar (mol/L)?", step=0.01)

# Verificación
if st.button("Verificar respuesta"):
    # Cálculo correcto
    moles = masa / peso_molar
    concentracion_molar = moles  # porque el volumen es 1 litro

    # Comparación con tolerancia de ±0.01 mol/L
    if abs(respuesta_usuario - concentracion_molar) <= 0.01:
        st.success(f"✅ ¡Correcto! La concentración es aproximadamente {concentracion_molar:.4f} mol/L.")
    else:
        st.error(f"❌ Incorrecto. La concentración correcta es {concentracion_molar:.4f} mol/L.")
