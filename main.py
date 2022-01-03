import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

dosya=pd.read_csv("Airports-Only.csv",encoding="latin-1")
st.title("All Airports On The World")
countries = dosya["Country"]
listcountries = list(countries.unique())
listcountries.insert(0, "All Countries")
col1,col2=st.columns(2)
with col1:
    stbox = st.selectbox("Select Country", listcountries)
    if stbox != "All Countries":
        dosya = dosya[dosya["Country"] == stbox]
with col2:
    listcity = list(dosya["City"].unique())
    listcity.insert(0, "All Cities")
    stcity = st.selectbox("Choose City", listcity)
    if stcity!="All Cities":
        dosya=dosya[dosya["City"]==stcity]
altitude=dosya["Altitude"]
minaltitude=min(altitude)
maxaltitude=max(altitude)
col1,col2=st.columns(2)
if minaltitude<maxaltitude:
    with col1:
        staltitude=st.slider("Min Altitude",minaltitude,maxaltitude)
    with col2:
        staltitude2=st.slider("Max Altitude",minaltitude,maxaltitude,value=maxaltitude)
    if staltitude2:
        dosya=dosya[dosya["Altitude"]<=staltitude2]
    if staltitude:
        dosya = dosya[dosya["Altitude"] >= staltitude]
else:
   st.write("This Column Is a Constant Of Value 'Min Altitude'")
col1,col2=st.columns(2)
with col1:
    #sttext=st.text_input("Enter Country Name: ")
    #if sttext:
        #dosya=dosya[dosya["Country"]==sttext]

    #listcolumns=list(dosya.columns)
    #selectcolumn=st.selectbox("Choose Column",listcolumns)
    #listrow=list(dosya[selectcolumn].unique())
    #rowst=st.selectbox("Choose Row",listrow)
    #dosya=dosya[dosya[selectcolumn]==rowst]
    #fig = px.scatter_mapbox(dosya, lat=dosya["Latitude"], lon=dosya["Longitude"], hover_name=dosya["City"], hover_data="",
                        #color_discrete_sequence=["fuchsia"], zoom=1, height=300)
    #fig.update_layout(mapbox_style="open-street-map")
    #fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #st.plotly_chart(fig,use_container_width=True)
    fig = px.scatter_mapbox(dosya, lat=dosya["Latitude"], lon=dosya["Longitude"], hover_name=dosya["City"],
                            hover_data="",
                            color_discrete_sequence=["#66ff99"], zoom=2, height=300)
    fig.update_layout(
        mapbox_style="white-bg",
        mapbox_layers=[
            {
                "below": 'traces',
                "sourcetype": "raster",
                "sourceattribution": "United States Geological Survey",
                "source": [
                    "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                ]
            }
        ])
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.dataframe(dosya)
    st.write("Number Of Airports")
    st.write(len(dosya["Airport_ID"]))



