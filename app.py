import streamlit as st
from random import randrange
import time 
import altair as alt
import pandas as pd



st.title("Remove Confusion")

option1 = st.text_input("Option 1","Sleep Downstairs")
option2 = st.text_input("Option 2","Sleep Upstairs")
noption1 = 0
noption2 = 0
n = st.number_input("How many times I should select",3)
if st.button("Select"):
    for i in range(n):
        option  = randrange(2)
        if option==0:
            noption1=noption1+1
            #st.title(option1)
        else:
            noption2=noption2+1
            #st.title(option2)
    
    if noption1>noption2:
        st.title(f'{option1} ({noption1} out of  {n})')
        st.balloons()
    else:
        st.title(f'{option2} ({noption2} out of  {n})')
        st.snow()
    source = pd.DataFrame({"category": [option1, option2], "value": [noption1, noption2]})
    st.altair_chart(alt.Chart(source).mark_arc().encode(
    theta=alt.Theta(field="value", type="quantitative"),
    color=alt.Color(field="category", type="nominal"),
    ))