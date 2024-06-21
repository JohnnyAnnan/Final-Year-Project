import streamlit as st
import pandas as pd

st.title('MACHINE LEARNING CUSTOMER SEGMENTATION SYSTEM')
st.subheader('For Sample Sales Dataset')

#st.header('header')
#st.text('text')

st.markdown('**bold** *italic* normal')
st.markdown('# h1 heading')
st.markdown('> blockquote')
st.markdown('[Example Link](https://www.kaggle.com/)')
st.markdown('___')
st.caption('caption')
st.markdown('___')
st.metric(label="Length", value="20m", delta="2m")
st.metric(label="Speed", value="40ms⁻¹", delta="-3ms⁻¹")

table = pd.DataFrame({"Column 1 (ID)": [1,2,3,4], "Column 2 (Item)": ["Bowl", "Cup", "Sugar", "Spoon"]})
st.table(table)
st.dataframe(table)

st.image('dataaesth.jpg', caption = 'Data Aesthetic', width = 430)