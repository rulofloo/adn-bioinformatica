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

### 5. Display Pie Chart using Altair
st.subheader('5. Grafico Circular')

import altair as alt

# Reshape the data for animated pie chart
df_pivot = df.melt('nucleotide', var_name='metric', value_name='value')

# Create animated pie chart
animated_pie_chart = alt.Chart(df_pivot).mark_arc().encode(
    alt.X('value:Q', stack='zero'),
    color='nucleotide:N',
    tooltip=['nucleotide', 'metric', 'value']
).properties(
    width=500,
    height=400
).transform_joinaggregate(
    total='sum(value)',
    groupby=['nucleotide']
).transform_calculate(
    percentage='datum.value / datum.total'
).encode(
    text=alt.Text('percentage:Q', format='.1%')
).configure_mark(
    opacity=0.8
)

# Adjust properties of the animated pie chart
animated_pie_chart = animated_pie_chart.properties(
    width=300,
    height=300
)

# Display the animated pie chart
st.altair_chart(animated_pie_chart, use_container_width=True)

p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count',
    column='nucleotide'
)

p = p.properties(
    width=alt.Step(80),  # controls width of bar
    height=alt.Step(40),  # controls height of bar
    column=alt.Column(
        spacing=10  # controls spacing between grouped bars
    )
)

st.header('Contacto para mas informacion')
st.markdown('**Creadores:** Samantha Duarte, Raul Delgado, Saul Peña ')
st.markdown('- **Correo electronico:** samduarteesp@gmail.com')
st.markdown('- **Numero de contacto:** +6441127839')


# In[ ]:




