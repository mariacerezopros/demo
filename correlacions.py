import streamlit as st
import numpy as np
import pickle
import xgboost
import pandas as pd
import shap
from streamlit_shap import st_shap

def correlacions():
    st.header('Correlacions')
    
    list = ['Escull la correlació que vols visualitzar', 
            'Consum d\'Aigüa - PIB', 'Consum d\'Aigüa - Atur', 
            'Consum d\'Aigüa - Immigració', 
            'Consum d\'Aigüa - Preu de la Llum']
    dataset = st.selectbox('', list)
    
    if dataset == 'Consum d\'Aigüa - PIB':
        st.image('pib.jpeg')
        st.success('Correlació positiva')
        st.caption('En aquest diagrama de dispersió podem veure com influeix el PIB (Producte Intern Brut) per habitant de cada municipi sobre el seu consum d\'aigua. A l\'eix vertical tenim el consum d\'aigua i a l\'eix horitzontal el PIB per habitant. Cada un dels cercles representa un municipi, mirant la llegenda podem veure de quin es tracta. Podem observar que els municipis amb més consum d\'aigua són majoritàriament aquells amb un PIB més elevat. Per tant, hi ha una correlació positiva  entre la riquesa del municipi i el consum d\'aigua; a més riquesa, més consum.')

    if dataset == 'Consum d\'Aigüa - Atur':
        st.image('atur.jpeg')
        st.success('Correlació negativa')
        st.caption('En aquest diagrama de dispersió podem veure com influeix el percentatge d\'atur de cada municipi sobre el seu consum d\'aigua. A l\'eix vertical tenim el consum d\'aigua per habitant del 2021 i a l\'eix horitzontal tenim el percentatge d\'atur de l\'any 2021. Cada un dels cercles representa un municipi, mirant la llegenda podem veure de quin es tracta. Podem observar clarament que els municipis amb més consum d\'aigua són majoritàriament aquells amb l\'índex d\'atur més baix i viceversa. Per tant, hi ha una correlació negativa bastant alta entre aquests factors; a més atur, més consum d\'aigua.')

    if dataset == 'Consum d\'Aigüa - Immigració':
        st.image('immigrants.jpeg')
        st.success('Correlació negativa')
        st.caption('En aquest diagrama de dispersió podem veure com influeix el percentatge d\'immigració de cada municipi sobre el seu consum d\'aigua. A l\'eix vertical tenim el consum d\'aigua per habitant del 2021 i a l\'eix horitzontal tenim el percentatge d\'immigració de l\'any 2021. Cada un dels cercles representa un municipi, mirant la llegenda podem veure de quin es tracta. Podem observar clarament que els municipis amb més consum d\'aigua són majoritàriament aquells amb l\'índex d\'atur més baix i viceversa. Per tant, hi ha una correlació negativa entre aquests factors bastant alta.')

    if dataset == 'Consum d\'Aigüa - Preu de la Llum':
        st.image('preullum.jpeg')
        st.error('Sense correlació')
        st.caption('En aquest diagrama de dispersió podem veure com influeix el preu de la llum de cada mes del 2021 sobre el consum mitjà d\'aigua. A l\'eix vertical tenim el consum d\'aigua per habitant del 2021 (en aquest cas és el consum mitjà de tots els municipis) i a l\'eix horitzontal tenim el preu de la llum mensual de l\'any 2021. Cada un dels cercles representa un mes de l\'any, mirant la llegenda podem veure de quin es tracta. Podem observar lleugerament que els mesos amb el preu de la llum més alt són aquells amb un consum d\'aigua més baix. Tot i això no podem detectar una clara correlació; veiem que alguns dels punts es troben repartits seguint un comportament bastant aleatori.')