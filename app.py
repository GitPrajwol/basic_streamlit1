import pandas as pd
import seaborn as sns 
import streamlit as st
df=sns.load_dataset('penguins')
st.dataframe(df)
st.table(df)
st.metric(
    label="Revenue",
    value="$1.2M",
    delta="+12%"
)