import streamlit as st
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("Kelompok 24")
st.markdown("""
1. Hasna Nurul Azmi Pranindya - 0110122254
2. Dimas Julian
3. Fadlan
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]              
                  )

st.line_chart(df)
