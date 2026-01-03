import streamlit as st
import matplotlib.pyplot as plt

st.title("Praktikum 8 - Kelompok 24")
st.markdown("""
            1. Hasna Nurul Azmi Pranindya - 0110122254
            """)

#data partisipasi siswa
kegiatan = ["Olahraga", "Seni", 'Musik', 'Debat']
persentase = [35, 25, 20, 20]

#fungsi
def plot_pie_chart(labels, data):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Persentase Partisipasi Siswa dalam Kegiatan Ekstrakulikuler')
    st.pyplot(fig)

#streamlit interface

st.title("Visualisasi Data Kegiatan Ekstrakulikuler")
st.subheader("Pie Chart Sederhana")
plot_pie_chart(kegiatan, persentase)

#kustomisasi
def plot_customized_pie(labels, data):
    colors = ['gold', 'lightblue', 'lightgreen', 'coral']
    explode = [0.1, 0, 0, 0]

    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)
    ax.set_title('Kustomisasi Pie Chart')
    st.pyplot(fig)

#streamlit kustomisasi
st.subheader("Kustomisasi Pie Chart")
plot_customized_pie(kegiatan, persentase)


#multiple pie chart
def plot_multiple_pie():
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

#data kelompok 1
    kegiatan_1 = ['Olahraga', 'Seni']
    persentase_1 = [40, 60]

#data kelompok 2
    kegiatan_2 = ['Musik', 'Debat']
    persentase_2 = [50, 50]

#pie chart untuk kelompok 1
    axs[0].pie(persentase_1, labels=kegiatan_1, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightblue'])
    axs[0].set_title('Partisipasi: Kelompok 1')

#pie chart untuk kelompok 2
    axs[1].pie(persentase_2, labels=kegiatan_2, autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'coral'])
    axs[1].set_title('Partisipasi: Kelompok 2')

    st.pyplot(fig)
#streamlit multiple
st.subheader("Multiple Pie Chart")
plot_multiple_pie()

