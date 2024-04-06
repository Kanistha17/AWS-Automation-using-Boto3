import aws_session_state
import streamlit as st
from boto3_features import DyanmoDB_create_table,DyanmoDB_put_item,DynamoDB_list_tables,DynamoDB_delete_table,DynamoDB_view_table

def main():
    aws_session_state.common_sidebar()

    choice=st.sidebar.selectbox(label="Select Dynamo DB Features",placeholder="Choose an option",index=None,options=["Create Table","Insert Data","List Dynamo DB Tables","Delete table","View table"])

    if choice=="Create Table":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(DyanmoDB_create_table.create_DyTable(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")
            
    elif choice=="Insert Data":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(DyanmoDB_put_item.putItem(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

    elif choice=="List Dynamo DB Tables":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            tables=(DynamoDB_list_tables.get_tables(st.session_state["aws_session_key"]))
            st.write(f"DynamoDB tables are : \n {tables}")
        else:
            st.write("AWS session Error")

    elif choice=="Delete table":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(DynamoDB_delete_table.delete_table(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

    elif choice=="View table":
        if ("aws_session_key" in st.session_state and st.session_state["aws_session_key"] is not None):
            st.write(DynamoDB_view_table.view_data(st.session_state["aws_session_key"]))
        else:
            st.write("AWS session Error")

if __name__=="__main__":
    main()