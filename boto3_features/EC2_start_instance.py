import streamlit as st
from boto3_features import EC2_list_instances


def start_instance(aws_sess):

    EC2_list_instances.list_instances(aws_sess)
    
    ec2_client = aws_sess.client(service_name="ec2")
    
    instances_input = st.text_input("Enter list of instance ids separated by commas (,) ",key="start_ec2_list_id",value=None)
    if instances_input != None:
        instance_ids = [item.strip() for item in instances_input.split(',')]
        print("length - ",len(instance_ids))
        response = ec2_client.start_instances(InstanceIds=instance_ids)
        return(f"EC2 instances with IDs {instance_ids} started.")
    return



    