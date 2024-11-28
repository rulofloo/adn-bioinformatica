#!/usr/bin/env python
# coding: utf-8

# In[2]:


######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Page Title
######################

image = Image.open('Nucleotide.jpeg')

st.image(image, use_column_width=True)
st.write("""
<style>
h1 {
    color: #08g24d;
    font-size: 32px;
    text-align: center;
    margin-bottom: 20px;
}

h2 {
    color: #0191h6;
    font-size: 24px;
    margin-bottom: 10px;
}

.subheader {
    color: #hj95il;
    font-size: 18px;
    margin-bottom: 5px;
}

.output {
    margin-top: 30px;
}

table.dataframe {
    border-collapse: collapse;
    margin-top: 10px;
}

table.dataframe th, table.dataframe td {
    border: 20px solid #ddd;
    padding: 6px;
    text-align: left;
}

table.dataframe th {
    background-color: Fore.RED;
}

.chart {
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

st.write("""
# ADN 
esta app fue generada por alumnos de bioinformatica, facilitando la rama de informacion
de los lectores interesados en enriquecer su conocimiento sobre el ADN

***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('SELECCIONA UNA SECUENCIA DE ADN')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input DNA sequence
st.header('Entrada (ADN)')
sequence

## DNA nucleotide count
st.header('SALIDA (composicion de nucleotidos de ADN)')


# 1. Imprimir diccionario
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader('1. Imprimir diccionario')
    def DNA_nucleotide_count(seq):
        d = dict([
            ('A', seq.count('A')),
            ('T', seq.count('T')),
            ('G', seq.count('G')),
            ('C', seq.count('C'))
        ])
        return d

    X = DNA_nucleotide_count(sequence)
    st.write(X)

with col2:
    # 2. Print text
    st.subheader('2. Imprimir texto')
    st.write('Hay ' + str(X['A']) + ' adenina (A)')
    st.write('Hay ' + str(X['T']) + ' timina (T)')
    st.write('Hay ' + str(X['G']) + ' guanina (G)')
    st.write('Hay ' + str(X['C']) + ' citosina (C)')

with col3:
    # 3. Display DataFrame
    st.subheader('3. Esquema de visualizacion')
    df = pd.DataFrame.from_dict(X, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'nucleotide'})
    st.write(df)

# Add CSS styling for subheaders
st.markdown(
    """
    <style>
    .stHeader > .deco-btn-container > div {
        display: inline-block;
        margin-right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

### 4. Display Bar Chart using Altair
st.subheader('4. Grafico de barras')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)


st.write("""
# ¿Como funciona el ADN? 
La principal función del ADN es almacenar y transmitir la información genética. El ADN se encuentra en el núcleo de las 
células (en organismos eucariotas) y en el citoplasma (en organismos procariotas). Esta información genética se usa para 
sintetizar proteínas, que son esenciales para el funcionamiento y la estructura de las células y organismos.

***
""")


st.write("""
# Transcripción y Traducción (Expresión genética) 
El proceso mediante el cual la información contenida en el ADN se convierte en proteínas se lleva a cabo en dos etapas principales:

Transcripción: Durante la transcripción, una porción del ADN (un gen) se copia en una molécula de ARN mensajero (ARNm). Este 
ARN es una versión complementaria de una de las cadenas de ADN y es el que llevará la información del gen desde el núcleo 
a los ribosomas en el citoplasma.

Traducción: En los ribosomas, la secuencia de bases del ARNm se traduce en una secuencia de aminoácidos, que luego se ensamblan 
para formar una proteína. Cada tres bases del ARNm (un codón) codifican un aminoácido específico.

***
""")

st.write("""
# Genes y Cromosomas 
Los genes son segmentos específicos de ADN que contienen la información para la producción de proteínas o ARN funcionales. Los 
genes están organizados en estructuras llamadas cromosomas. En los seres humanos, por ejemplo, hay 23 pares de cromosomas en 
cada célula (en total, 46 cromosomas), y cada uno contiene miles de genes.

***
""")

st.write("""
# Variabilidad y Herencia
Las diferencias en las secuencias de ADN entre individuos se deben a las mutaciones o a la variabilidad genética heredada de 
los padres. Estas diferencias son las que dan lugar a las características físicas y biológicas únicas de cada individuo. El ADN 
se transmite de padres a hijos en el proceso de reproducción, lo que asegura que las características genéticas se hereden.

***
""")

st.write("""
# Resumen
En resumen, el ADN es el "manual de instrucciones" para la vida. Su secuencia de nucleótidos determina las características 
biológicas de un organismo y es responsable de las funciones celulares esenciales. La replicación, transcripción y traducción 
del ADN son los procesos mediante los cuales la información genética se utiliza para mantener y perpetuar la vida.

Si tienes más preguntas sobre algún aspecto específico del ADN o su función, ¡estaré encantado de responder! Para mas informacion
y dudas en la arte inferior de la pagina se encuentra en la parte inferior

***
""")


st.header('Contacto para mas informacion')
st.markdown('**Creadores:** Samantha Duarte, Raul Delgado, Saul Peña ')
st.markdown('- **Correo electronico:** samduarteesp@gmail.com')
st.markdown('- **Numero de contacto:** +6441127839')


# In[ ]:




