import streamlit as st
import pandas as pd
import numpy as np



st.title("Map Chart")
st.write("Kelompok 24")
st.markdown("""
1. Hasna Nurul Azmi Pranindya - 0110122254
2. Dimas Julian
3. Fadlan
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078], 
    columns=["latitude", "longitude"]
    )

st.map(df)
