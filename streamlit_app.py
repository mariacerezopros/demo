import streamlit as st
import pandas as pd
#from streamlit_option_menu import option_menu
from dades import dades
from correlacions import correlacions
from accions import accions

st.set_page_config(
    page_title='AQUALITY',
    page_icon='💧',
    layout='wide',
    initial_sidebar_state='expanded',
)

st.image('logo.jpeg', width=5, use_column_width=True)
page = st.sidebar.selectbox("Menu Principal", ('Dades', 'Correlacions','Pla d\'Accions'))
#with st.sidebar:
    #page = option_menu('Menú Principal', ['Dades', 'Correlacions', 'Pla d\'Accions'], 
        #icons=['eye', 'bar-chart-line', 'arrow-bar-up'], menu_icon="cast", default_index=0,
        #styles={
        #"container": {"padding": "0!important", "background-color": "#fafafa"},
        #"icon": {"color": "green", "font-size": "20px"}, 
        #"nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        #"nav-link-selected": {"background-color": "#679cbe"},
    #})


if page == 'Dades':
    dades()

if page == 'Correlacions':
    correlacions()

if page == 'Pla d\'Accions':
    accions()