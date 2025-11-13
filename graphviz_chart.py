import streamlit as st # type: ignore
import graphviz_chart as graphviz

st.title("Graphviz Chart")
st.write("Kelompok 24")
st.markdown("""
1. Hasna Nurul Azmi Pranindya - 0110122254
2. Dimas Julian
3. Fadlan
""")

st.graphviz_chart("""
                  digraph{
                  "Training Data" -> "ML Algorithm"
                  "ML Algorithm" -> "Model"
                  "Model" -> "Result Forecasting"
                  "New Data" -> "Model"}
                  """)