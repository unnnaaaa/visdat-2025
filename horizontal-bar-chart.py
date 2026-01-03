import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("Penjualan Smartphone Berdasarkan Merk")
st.subheader("Horizontal Bar Chart Sederhana")
st.markdown("""
Kelompok 24 :
            1. Hasna Nurul Azmi Pranindya - 0110122254
""")

#data penjualan
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales = [350, 420, 300, 280]

#horizontal bc
fig, ax, = plt.subplots()
y = np.arange(len(brands)) #batang
ax.barh(y, sales, color='skyblue')
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Smartphone Sales by Brand')

#interface
st.pyplot(fig)

#warna batang
colors = ['blue', 'green', 'orange', 'red']

fig, ax = plt.subplots()
ax.barh(y, sales, color=colors)

#tambah nilai pd batang
for i, v in enumerate(sales):
    ax.text(v + 10, i, str(v), color='black', va='center') #teks
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Customized Smartphone Sales by Brands')

st.pyplot(fig)

st.subheader("Multiple Horizontal Bar Chart")
#data penjualan
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
q1_sales = [350, 400, 300, 250]
q2_sales = [370, 420, 310, 280]

bar_width = 0.4 #lebar batang
y = np.arange(len(brands))

fig, ax = plt.subplots()

#multiple horiz-bc

ax.barh(y - bar_width / 2, q1_sales, height=bar_width, label='Q1 Sales', color='skyblue')
ax.barh(y + bar_width / 2, q2_sales, height=bar_width, label='Q2 Sales', color='salmon')

#penyesuaian tampilan
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Smartphone Sales by Brand (Multiple Periods)')
ax.legend()

st.pyplot(fig)