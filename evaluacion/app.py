import streamlit as st
import pandas as pd


data = {
    "Date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04", "2024-01-05"],
    "Product": ["Laptop", "Phone", "Mouse", "Keyboard", "Tablet"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [1000, 700, 25, 50, 400],
    "Quantity": [2, 3, 10, 5, 4],
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

# Guardar el archivo CSV en el mismo directorio
df.to_csv("sales_data.csv", index=False)

st.title("Análisis Básico de Ventas")


df = pd.read_csv('sales_data.csv')

st.subheader("Datos Completos")

st.dataframe(df)


st.sidebar.header("Filtros")

category = st.sidebar.selectbox("Selecciona una categoría", df["Category"].unique())


min_price = float(df["Price"].min())
max_price = float(df["Price"].max())
price_range = st.sidebar.slider("Rango de precios", min_price, max_price, (min_price, max_price))

filtered_df = df[
    (df["Category"] == category) &
    (df["Price"] >= price_range[0]) &
    (df["Price"] <= price_range[1])
]

st.subheader("Datos Filtrados")
st.write(f"Número de registros: {filtered_df.shape[0]}")
st.dataframe(filtered_df)


st.subheader("Estadísticas")
if not filtered_df.empty:
    total_sales = filtered_df["Total_Sales"].sum()
    avg_price = filtered_df["Price"].mean()

    st.metric("Total de Ventas", f"${total_sales:,.2f}")
    st.metric("Precio Promedio", f"${avg_price:,.2f}")
else:
    st.write("No hay datos para los filtros seleccionados.")
