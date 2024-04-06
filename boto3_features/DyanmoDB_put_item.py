import boto3
import json
import streamlit as st
from boto3_features import DynamoDB_list_tables


def putItem(aws_sess):
    dynamodb_client = aws_sess.client(service_name="dynamodb")
    tables_list = DynamoDB_list_tables.get_tables(aws_sess)
    st.write(f''' Tables present in DynamoDB :
             {tables_list}''')
    table_name = st.text_input("Enter table name",key="existing_table_id")
    
    with open('app1/data.json','r') as f:
        table_data = json.load(f)

    if table_name:

        if table_name in tables_list:

            for key, value in table_data.items():
                dynamodb_client.put_item(
                    TableName=table_name,
                    Item={
                        'original_part_number': {'S': key},
                        "processorBrand": {'S': value['processorBrand']},
                        "processorNumber":{'S': value['processorNumber']},
                        "operatingSystem": {'S': value['operatingSystem']},
                        "oemName": {'S': value['oemName']},
                        "formFactor": {'S': value['formFactor']},
                        "storageType": {'S': value['storageType']},
                        "storageSize": {'S': value['storageSize']},
                        "screenSize": {'S': value['screenSize']},
                        "gpuQuantity": {'S': str(value['gpuQuantity'])},
                        "gpuType": {'S': value['gpuType']},
                        "gpu_model_number": {'S': value['gpu_model_number']}
                    }
                )

            return(f"Items inserted into table - {table_name}")
        else:
            return(f"{table_name} table not present, create table first.")
        
    return