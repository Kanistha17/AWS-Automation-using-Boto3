import boto3
import streamlit as st
from boto3_features import DynamoDB_list_tables


def view_data(aws_sess):

    dynamodb_client = aws_sess.client(service_name="dynamodb")

    tables_list = DynamoDB_list_tables.get_tables(aws_sess)
    st.write(f''' Tables present in DynamoDB :
             {tables_list}''')
    table_name = st.text_input("Enter table name",key="view_table")

    if len(table_name)>0:
        if table_name in tables_list:
            response = dynamodb_client.scan(
                TableName=table_name
            )
            items = response['Items']
            return(f"{items}")
        else:
            return("No such table found !!")
    return
