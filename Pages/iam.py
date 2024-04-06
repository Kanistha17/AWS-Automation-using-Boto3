import aws_session_state
import streamlit as st
from boto3_features import IAM_list_users

def main():
    aws_session_state.common_sidebar()

    choice=st.sidebar.selectbox(label="Select IAM Features",placeholder="Choose an option",index=None,options=["List IAM Users","List IAM Roles"])

    if choice=="List IAM Users":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(IAM_list_users.get_iam_users(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

if __name__=="__main__": 
    main()