import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('India.csv')

states = list(df['State'].unique())
states.insert(0, 'All States')

st.set_page_config(layout='wide')
st.title("Geographic Visualization of India")
st.caption("An interactive dashboard for visualizing India's demographic data")
st.sidebar.title('Data Visuzalization of India')
selected_state = st.sidebar.selectbox('Select State', states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[[5] + list(range(11, len(df.columns)))]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[[5] + list(range(11, len(df.columns)))]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represents Primary Parameter')
    st.text('Color represents Secondary Parameter')
    if selected_state == 'All States':
        fig = px.scatter_mapbox(df,lat='Latitude',lon='Longitude',zoom=3.2,size=primary,color=secondary,mapbox_style="carto-positron",width=3000,height=600,color_continuous_scale="Plasma",hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',zoom=5,size=primary,color=secondary,mapbox_style="carto-positron",width=3000,height=600,color_continuous_scale="Plasma",hover_name='District')
        st.plotly_chart(fig,use_container_width=True)

