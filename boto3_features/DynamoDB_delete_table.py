import boto3
import streamlit as st
from boto3_features import DynamoDB_list_tables


def delete_table(aws_sess):

    dynamodb_client = aws_sess.client(service_name="dynamodb")

    tables_list = DynamoDB_list_tables.get_tables(aws_sess)
    st.write(f''' Tables present in DynamoDB :
             {tables_list}''')
    table_name = st.text_input("Enter table name",key="delete_table")

    if len(table_name)>0:
        if table_name in tables_list:
            response = dynamodb_client.delete_table(
                TableName=table_name
            )
            return(f"{table_name} - Table deleted successfully.")
        else:
            return("No such table found !!")
    return
