import streamlit as st
import pandas


st.set_page_config(layout="wide")

st.title("The Best Company")
content = "As the name says, this is the Best Company."
st.write(content)
st.header("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([2,1,2,1,2])
df = pandas.read_csv("data.csv", sep=",")
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[-4:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/" + row["image"])
