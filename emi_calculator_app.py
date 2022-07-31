import streamlit as st
def calculate_emi(p, n, r):
	emi=p*(r/100)*(1+(r/100))**n/((1+(r/100))**n)-1
st.slider()