import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Praktikum 8 - Kelompok 24")
st.markdown("""
            1. Hasna Nurul Azmi Pranindya - 0110122254
            """)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des'] 
shoes = [500, 600, 700, 800, 650, 700, 850, 900, 750, 800, 950, 1000]
sandals = [300, 350, 400, 450, 500, 300, 600, 400, 400, 700, 750, 500]
socks = [200, 250, 300, 350, 300, 400, 450, 500, 600, 700, 750, 800]

#fungsi area chart
def plot_area_chart(selected_products):
    plt.figure(figsize=(10, 6))


    if 'Sepatu' in selected_products:
        plt.fill_between(months, shoes, color="blue", alpha=0.5, label="Sepatu")
    if 'Sandal' in selected_products:
        plt.fill_between(months, shoes, color="green", alpha=0.5, label="Sandal")
    if 'Kaos Kaki' in selected_products:
        plt.fill_between(months, shoes, color="orange", alpha=0.5, label="Kaos Kaki")
    
    plt.title("Area Chart Penjualan Bulanan")
    plt.xlabel('Bulan')
    plt.ylabel('Unit Terjual')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle="--", alpha=0.6)
    plt.legend()

    st.pyplot(plt)

def main():
    st.title("Visualisasi Penjualan Bulanan")
    st.sidebar.title("Pengaturan Grafik")

    #filter
    st.sidebar.markdown("### Pilih Produk")
    products = ['Sepatu', 'Sandal', 'Kaos Kaki']
    selected_products = st.sidebar.multiselect("Produk ang akan ditampilkan", products, default=products)

    st.markdown("### Area Chart Penjualan")
    plot_area_chart(selected_products)

if __name__ == "__main__":
    main()
    
    