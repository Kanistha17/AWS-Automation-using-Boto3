import boto3
import os

def get_tables(aws_sess):

    dynamodb = aws_sess.client(service_name="dynamodb")
    response = dynamodb.list_tables()

    tables=[]

    for table_name in response['TableNames']:
        tables.append(table_name)

    return tables