import streamlit as st

def show_home():
    st.markdown("<h1>THETA - Flood AI Competition</h1>", unsafe_allow_html=True)
    st.markdown("<h3>IIEC IIT Gandhinagar</h3>", unsafe_allow_html=True)
    st.write("-----")

    st.write("""
    ## Welcome to our Flood Monitoring and Prediction Dashboard!
    We are Team **THETA**, participating in the **Flood AI Competition** organized by IIEC IIT Gandhinagar.
    
    Our focus is on predicting flood risks using advanced machine learning models, leveraging a well-curated dataset of Kozhikode/Calicut.
    
    This project aims to provide actionable insights and early warnings to mitigate the impacts of flooding in vulnerable regions.
    """)

    st.write("-----")

    st.write("### Team Members:")
    st.markdown("""
    - **Raviraj**: Conceptualisation, Data management and Formal analysis
    - **Mayank**: Conceptualisation, UI/UX and Machine Learning
    - **Mannat**: Conceptualisation
    - **Arjun**: Conceptualisation
    """)

    st.write("### Acknowledgments")
    st.markdown("""
    We would like to express our gratitude to our mentors, organizers, and fellow participants for their support and collaboration throughout this competition.
    """)
    st.write("-----")
