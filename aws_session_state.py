import streamlit as st

def common_sidebar():
    # common sidebar content : AWS session state Inactive or Active
    st.sidebar.title("AWS Session State")
    # st.sidebar.header("Navigation")
    # Add more sidebar elements as needed

    
    # Set the flag
    flag = "ACTIVE" if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None) else "INACTIVE"
    # Define the color based on the value
    color = "green" if flag == "ACTIVE" else "red"
    markdown_str = f'<font color="white">AWS Session: </font><font color="{color}">{flag}</font>'
    st.sidebar.markdown(markdown_str, unsafe_allow_html=True) 

