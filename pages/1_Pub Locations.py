import streamlit as st
import pandas as pd
import numpy as np

import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "resources_data_pub_cleaned.csv")

st.title("Pub Locations")

df=pd.read_csv(DATA_PATH)

searchtype = st.selectbox("Select a column based on information of Area", ["postcode", "local_authority"])
selecting_area=st.selectbox("Select the information you had from the drop column",df[searchtype].unique())

df1=df[df[searchtype]==selecting_area]
df2=df1[['latitude','longitude']]

st.header("INFORMATION ABOUT THE PUB")

st.write(df1)

st.map(df2)

