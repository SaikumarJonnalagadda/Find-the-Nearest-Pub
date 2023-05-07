import streamlit as st
import pandas as pd
import numpy as np

import scipy.spatial.distance as dist
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "resources_data_pub_cleaned.csv")

st.title("Findig Neareast Pub")

df=pd.read_csv(DATA_PATH)


latitude = st.number_input("Enter your Latitude:")
longitude = st.number_input("Enter your Longitude:")
btn_click1 = st.button("Get the Pubs")

df["distance"] = df.apply(lambda row: dist.euclidean((latitude, longitude), (row["latitude"], row["longitude"])), axis=1)


df = df.sort_values(by=["distance"])
df1=df[['latitude','longitude']]
pubs_near=df1.head(5)

if btn_click1 == True:

    st.map(pubs_near)

    st.header("INFORMATION ABOUT THE PUBS")

    st.write(df.head(5))

