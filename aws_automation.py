import os
import boto3
import streamlit as st

import app1
import boto3_features
import aws_session_state
from dotenv import load_dotenv

load_dotenv()

def page_config():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="expanded",
        page_title="AWS Automation App",
        page_icon="😎"
    )

def page_content():
    st.write("WELCOME TO AWS Automation App")

    aws_access_key_id=st.text_input("Enter AWS Access Key ID",type="password",key="access_key_id",value=os.environ.get("aws_access_key_id"))
    aws_secret_access_key=st.text_input("Enter AWS Secreat Access Key",type="password",key="secret_access_key",value=os.environ.get("aws_secret_access_key"))
    aws_region=st.text_input("Enter AWS region",type="default",key="region",value=os.environ.get("region"))

    if "aws_session_key" not in st.session_state:
        st.session_state["aws_session_kaye"]=None

    if st.button("Connect to AWS Boto3 Session"):
        st.session_state["aws_session_key"] = boto3.session.Session(aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=aws_region)

    if st.button("Clear AWS Session"):
        if "aws_session_key" in st.session_state:
            st.session_state["aws_session_key"]=None

    aws_session_state.common_sidebar()

    return st.session_state["aws_session_key"] if "aws_session_key" in st.session_state else None

def main():

    page_config()
    page_content()

    

if __name__=="__main__":
    main()