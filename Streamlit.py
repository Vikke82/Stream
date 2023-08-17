#pip install streamlit
#streamlit hello
#These might need admin 
#https://streamlit.io/
#Note Python version or virtual environment
#python -m streamlit run your_script.py when from command prompt
#streamlit run your_script.py from vs code
#crtl+c to stop run

import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff#pip install plotly
from pandas.api.types import is_numeric_dtype

st.title("Document titles", anchor=None)
st.write("Hewllo")
st.write('''
#My app
# Testing Streamlit
''')


st.header('Electric prices')
st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')



#markdowns
#import streamlit as st

st.markdown('Streamlit can **_use_ markdowns**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

'''Adding a widget is the same as declaring a variable. 
No need to write a backend, define routes, handle HTTP requests, 
connect a frontend, write HTML, CSS, JavaScript, ...'''

file = st.file_uploader("Pick a map data in excel or csv-file")
try:
    df2 = pd.read_excel(file)
    st.header(file.name)
    st.dataframe(df2)
    st.write("Excel picked")
except:
    try:
        df2 = pd.read_csv(file)
        st.header(file.name)
        st.dataframe(df2)
        st.write("CSV picked")
    except:
        st.write("Error in Pick excel or csv file")


st.header("Plot map if data available or data columns")

#plotting map
try:
    st.map(df2)
except:
    st.write("No map data")
    try:
        st.text_input("Column", key="name")
        # You can access the value at any point with and also with some event:
        st.write(df2[st.session_state.name])
        
    except:
        st.write("Error")




file2 = st.file_uploader("Pick data")
file2_fetched = False
try:
    df = pd.read_csv(file2, parse_dates=['Time'])
    file2_fetched = True
except:
    try:
        df = pd.read_csv(file2)
        file2_fetched = True
    except:
        st.write("No data")

if file2_fetched == True:
    st.header('Dataframe as interactive dataframe')
    st.dataframe(df)  # Same as st.write(df)

    start_date, end_date = st.select_slider(
        'Select a time range',
        options=list(df['Time']),
        value=(df['Time'].min(), df['Time'].max()))

    mask = (df['Time'] > start_date) & (df['Time'] <= end_date)

    st.line_chart(df.loc[mask], x="Time", y="Price")


group_labels = []
hist_data = []
for col in df.columns:
    if is_numeric_dtype(df[col]):
        group_labels.append(col)
        hist_data.append(df[col])

st.write(group_labels)

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels)

# Plot!
st.plotly_chart(fig, use_container_width=True)