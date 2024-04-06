import boto3
import os
import streamlit as st


def create_instance(aws_sess):

    ec2_client = aws_sess.client(service_name="ec2")

    # ec2=boto3.resource('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

    ami_id=st.text_input("Enter AMI ID",key="ami_id",value="ami-051f8a213df8bc089")
    count=st.text_input("Enter number of instances to be created",value=None)

    submit_button = st.button('Submit',key="create_instance_submit")


    instance_params = {'ImageId': ami_id,  # Specify the AMI ID
                        'InstanceType':'t2.micro',          # Specify the instance type
                        'MinCount': count,                         # Minimum number of instances to launch
                        'MaxCount': count                          # Maximum number of instances to launch
                        }
    
    instances = ec2_client.run_instances(**instance_params)
    return(f"New EC2 instances created with IDs: {[instance.id for instance in instances]}")

    