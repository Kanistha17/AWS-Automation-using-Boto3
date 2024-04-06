import glob
import json
import trafilatura
import os
import shutil

def getKeyListFromDict(dict):
    return list(dict.keys())

def getProductIdentifiers(path):
    with open(path,'r') as file:
        dictData=json.load(file)

    productIdentifiers = getKeyListFromDict(dictData)
    return productIdentifiers

def extractText(url,mpn):

    try:
        downloaded = trafilatura.fetch_url(url)
        result = trafilatura.extract(downloaded)
        if result==None:
            print(f"\"None\" returned for MPN : {mpn}\n\t URL : {url}")
            return ""
        return result
    except Exception as e:
        print(f"Error for {mpn}, URL : {url} : {e}")
        return ""

def getWebData(productIdentifiers,inputDir,outputFile,apiType,titleKey,snippetKey,linkKey,items):

    # files=glob.glob(f'{inputDir}/*.json')
    dataDict={}

    for mpn in productIdentifiers:
        with open(f"{inputDir}/{mpn}.json",'r') as f1:
            data = json.load(f1)

        text=""
        data=data['webPages'] if apiType=="bing" else data

        for webpage in data.get(items,[]):
            name = webpage[titleKey]
            snippet = webpage[snippetKey]
            url = webpage[linkKey]

            # if relevant then extract text
            result = extractText(url,mpn)
            
            text=text+"\n"+name+"\n"+snippet+"\n"+result
        dataDict[mpn]=text
        print(f"Data extracted for {mpn}")

    with open(f'{outputFile}', 'w',encoding='utf-8') as json_file:
        json.dump(dataDict, json_file, indent=4, ensure_ascii=False)

    return

def main():

    dataPath = "app1/data/data.json"
    inputDirBing="app1/data/api_results"
    outputFileBing = "app1/data/web_data.json"

    productIdentifiers = getProductIdentifiers(dataPath)
    
    # getWebData(productIdentifiers,inputDirGoogle,outputFileGoogle,"google","title","snippet","link","items")
    getWebData(productIdentifiers,inputDirBing,outputFileBing,"bing","name","snippet","url","value")

if __name__=="__main__":
    main()






