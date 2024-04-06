import boto3
import os
import streamlit as st


def list_instances(aws_sess):

    ec2_client = aws_sess.client(service_name="ec2")
    
    response = ec2_client.describe_instances()

    # Extract instance information
    instances = []
    c=0
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance)
            c+=1

    st.write(f"Total Instances : {c}\n\n")
    # Print instance information
    for instance in instances:
        st.write(f"Instance ID: {instance['InstanceId']}, State: {instance['State']['Name']}\n")
        
    return