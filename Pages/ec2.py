import streamlit as st
import boto3
from boto3_features import EC2_create_instance, EC2_list_instances, EC2_terminate_instance, EC2_stop_instance, EC2_start_instance, EC2_reboot_instance

import aws_session_state

def main():
    aws_session_state.common_sidebar()

    choice=st.sidebar.selectbox(label="Select EC2 Features",placeholder="Choose an option",index=None,options=["Create EC2 instance","List EC2 instances","Terminate EC2 instance","Stop EC2 instance","Start EC2 instance","Reboot EC2 instance"])

    if choice=="Create EC2 instance":

        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(EC2_create_instance.create_instance(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

    elif choice=="List EC2 instances":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(EC2_list_instances.list_instances(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

    elif choice=="Terminate EC2 instance":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(EC2_terminate_instance.terminate_instance(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")
    
    elif choice=="Stop EC2 instance":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(EC2_stop_instance.stop_instance(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

    elif choice=="Start EC2 instance":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(EC2_start_instance.start_instance(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

    elif choice=="Reboot EC2 instance":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(EC2_reboot_instance.reboot_instance(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

if __name__=="__main__": 
    main()