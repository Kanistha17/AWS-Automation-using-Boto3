import getpass as gpass
import os
import pandas as pd
import requests
import json
import shutil

def getKeyListFromDict(dict):
    return list(dict)

def getProductIdentifiers(path):
    with open(path,'r') as file:
        dictData=json.load(file)

    productIdentifiers = getKeyListFromDict(dictData)
    return productIdentifiers

def getSearchData(api_key,endpoint,maxItemCount,productIdentifiers,mkt,outputDir):

    if os.path.exists(outputDir):
        shutil.rmtree(outputDir)

    print(f"Creating directory '{outputDir}'...")
    os.mkdir(outputDir)

    headers = { 'Ocp-Apim-Subscription-Key': api_key }

    for mpn in productIdentifiers:
        query=f"Give product specifications for {mpn}"
        params = { 'q': query,"count":maxItemCount}
        response = requests.get(endpoint, headers=headers, params=params)

        print(response.content)
        
        if response.status_code==200:          
            with open(f"{outputDir}/{mpn}.json",'w') as json_file:
                json.dump(response.json(), json_file, indent=4)
            print(f"Success : {query}")
        else:
            print(f"Error retrieving for : {query}\nError Code : {response.status_code}")
    return

def main():

    dataPath = "app1/data/data.json"
    productIdentifiers = getProductIdentifiers(dataPath)

    api_key = os.environ.get("BING_SEARCH_V7_SUBSCRIPTION_KEY")
    endpoint = "https://api.bing.microsoft.com/v7.0/search"
    outputDir="app1/data/api_results"
    maxItemCount=5

    mkt=""
    # mkt = "en-IN"

    getSearchData(api_key,endpoint,maxItemCount,productIdentifiers,mkt,outputDir)
    

if __name__=="__main__": 
    main() 
