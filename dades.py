import streamlit as st
import pandas as pd

MAX_ROWS = 10000

def dades():
    st.header('Dades')

    consum = pd.read_csv('consum.csv', sep=';')
    pib = pd.read_csv('PIB.csv', sep=';')
    atur = pd.read_csv('atur.csv', sep=';')
    immigracio = pd.read_csv('immigracio.csv', sep=';')
    llum = pd.read_csv('preullum.csv', sep=';')

    list = ['Escull les dades que vols visualitzar', 'Consum d\'Aigua', 'PIB', 'Atur', 'Immigració', 'Preu de la Llum']
    dataset = st.selectbox('', list)
    
    if dataset == 'Consum d\'Aigua':
        st.caption('Consum total d\'aigüa mensual per municipis de l\'AMB (litres/mes). Any 2021')
        st.write(consum)

    if dataset == 'PIB':
        st.caption('PIB per càpita dels municipis de l\'AMB. Any 2021')
        st.write(pib)

    if dataset == 'Atur':
        st.caption('Índex d\'atur de cada municipi de l\'AMB. Any 2021')
        st.write(atur)

    if dataset == 'Immigració':
        st.caption('Índex d\'immigració de cada municipi de l\'AMB. Any 2021')
        st.write(immigracio)
        
    if dataset == 'Preu de la Llum':
        st.caption('Preu de la llum mensual. Any 2021')
        st.write(llum)
