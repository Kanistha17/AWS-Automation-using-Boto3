import boto3
import os


def get_iam_users(aws_sess):

    # aws_access_key_id=os.environ.get("aws_access_key_id")
    # aws_secret_access_key=os.environ.get("aws_secret_access_key")
    # region_name=os.environ.get("region")
    # aws_sess = boto3.session.Session(aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region_name)

    iam_console = aws_sess.client(service_name="iam")
    result = iam_console.list_users()

    iam_users_list=[]
    for each_user in result['Users']:
        iam_users_list.append(each_user['UserName'])
    return iam_users_list