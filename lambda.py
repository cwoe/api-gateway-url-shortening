import json
import boto3
import random
import string
import botocore

url = 'url.cwoellner.com'
bucket = 'url.cwoellner.com'

def createSiteId():
    s3 = boto3.resource('s3')
    hexcode = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8)) + '.html'
    try:
        s3.Object(bucket, hexcode).load()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return hexcode
        else:
            # Something else has gone wrong.
            raise
    else:
        return createSiteId()
    
    
def lambda_handler(event, context):
    
    longurl = event['queryStringParameters']['longurl']

    hexcode = createSiteId()
    
    pagecontent = '<head> <meta http-equiv="Refresh" content="0; URL=' + longurl + '"> </head>'
    bytestream = bytes(pagecontent.encode('UTF-8'))
    
    s3 = boto3.client('s3')
    s3.put_object(ACL='public-read', Bucket=bucket, Key=hexcode, Body=bytestream, ContentType="text/html")
    
    shorturl = 'https://' + url + '/' + hexcode
    response = {}
    response['shorturl'] = shorturl
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(response)
    }
