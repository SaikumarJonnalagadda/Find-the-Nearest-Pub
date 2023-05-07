import streamlit as st
import os
st.title("NEAREAST Pub FINDER")
st.header("JONNALAGADDA SAIKUMAR")
st.header("lets CONNECT:")
st.write("LINKDIN: [link](https://www.linkedin.com/in/saikumar-jonnalagadda-305003215)")
st.write("GITHUB: [link](https://github.com/SaikumarJonnalagadda)")
    
    

btn_click1 = st.button("ABOUT THIS APP!")


if btn_click1 == True:
    st.write("This application is used to find neareast pub location in United Kingdom")
    st.write("Through this application you can  know the following data of pubs in the United kingdom")
    st.write('''fsa_id
                name                  
                address           
                postcode             
                easting                
                northing                 
                latitude                 
                longitude                 
                local_authority''')