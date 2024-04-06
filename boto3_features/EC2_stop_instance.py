import streamlit as st
from boto3_features import EC2_list_instances


def stop_instance(aws_sess):

    EC2_list_instances.list_instances(aws_sess)
    
    ec2_client = aws_sess.client(service_name="ec2")
    
    instances_input = st.text_input("Enter list of instance ids separated by commas (,) to be deleted",key="terminate_ec2_list_id",value=None)
    if instances_input != None:
        instance_ids = [item.strip() for item in instances_input.split(',')]
        response = ec2_client.stop_instances(InstanceIds=instance_ids)
        return(f"EC2 instances with IDs {instance_ids} stoped.")
    return



    