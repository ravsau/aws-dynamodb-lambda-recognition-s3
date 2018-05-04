from __future__ import print_function

import boto3
from decimal import Decimal
import json
import urllib

print('Loading function')

rekognition = boto3.client('rekognition')

dynamo= boto3.resource('dynamodb')



def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})

    
    return response


# --------------- Main handler ------------------

def lambda_handler(event, context):
    '''Demonstrates S3 trigger that uses
    Rekognition APIs to detect faces, labels and index faces in S3 Object.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

   
    
    print (event)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        

        # Calls rekognition DetectLabels API to detect labels in S3 object
        response = detect_labels(bucket, key)
        
        toDynamo=[]
        
        for Label in response["Labels"]:
           # print (Label["Name"] + Label["Confidence"])
            
            print ('{0} - {1}%'.format(Label["Name"], Label["Confidence"]))
            
            Name= Label["Name"]
            Confidence = Label["Confidence"]
            if Confidence>70:
                toDynamo.append ( Name)
            
            
    
     
        
        table=dynamo.Table('Dynamo-Lambda')
        sendDynamo= table.put_item(
    TableName='Dynamo-Lambda',
    Item= {"key" : key , "Labels": toDynamo }) 
    
        return "hello"
    except Exception as e:
       
        raise e

