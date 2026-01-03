import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("Penjualan Smartphone Berdasarkan Merk")
st.subheader("Stacked Horizontal Bar Chart")
st.markdown("""
Kelompok 24 :
            1. Hasna Nurul Azmi Pranindya - 0110122254
""")


#data penjualan
brands = ['Brand A', 'Brand B', 'Brand C']
sales_2022 = [350, 450, 300]
sales_2023 = [400, 500, 320]

def create_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))
    ax.barh(y, sales_2022, color='skyblue', label='2022')
    ax.barh(y, sales_2023, left=sales_2022, color='salmon', label='2023')
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Smartphone Sales by Brand')
    ax.legend()
    return fig

#render chart
st.title("Smartphone Sales Visualization")
st.pyplot(create_stacked_bar_chart())

def create_custom_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    y = np.arange(len(brands))
    
    ax.barh(y, sales_2022, label='2022', color='blue', edgecolor='black', hatch='//')
    
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='green', edgecolor='black', hatch='\\\\')
    
    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Customized Smartphone Sales by Brand')
    ax.legend()

    # Tambahkan anotasi
    for i in range(len(brands)):
        ax.text(sales_2022[i] / 2, i, f'{sales_2022[i]}', va='center', color='white')
        ax.text(sales_2022[i] + sales_2023[i] / 2, i, f'{sales_2023[i]}',va='center', color='black'
        )

    return fig

st.pyplot(create_custom_stacked_bar_chart())

    