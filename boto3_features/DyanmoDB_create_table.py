import boto3
import pandas as pd
import json
import streamlit as st
from boto3_features import DynamoDB_list_tables


def create_DyTable(aws_sess):
    dynamodb_client = aws_sess.client(service_name="dynamodb")

    tables_list = DynamoDB_list_tables.get_tables(aws_sess)
    st.write(f''' Tables present in DynamoDB :
             {tables_list}''')
    table_name = st.text_input("Enter table name",key="insert_data_table")
    
    if table_name:
        if table_name in tables_list:
            st.write("Table already present")
        else:

            KeySchema = [
                {
                    'AttributeName': 'original_part_number',  
                    'KeyType': 'HASH'
                }
            ]

            AttributeDefinitions = [
                {
                    'AttributeName': 'original_part_number',
                    'AttributeType': 'S'
                }
            ]

            provisionedThroughput = {
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }

            table = dynamodb_client.create_table(
                TableName=table_name,
                KeySchema=KeySchema,
                AttributeDefinitions=AttributeDefinitions,
                ProvisionedThroughput=provisionedThroughput
            )

            return f"{table_name} created successfully"
    return 