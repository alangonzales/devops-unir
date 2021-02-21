import json
import boto3

def translate(event, context):
    text = event['pathParameters']['id']
    languageText = event['pathParameters']['language']

    
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')

    resultCompr = comprehend.detect_dominant_language(Text = text)

    translate = boto3.client('translate')
    result = translate.translate_text(Text=text,
                                      SourceLanguageCode=resultCompr["Languages"][0]["LanguageCode"],
                                      TargetLanguageCode=languageText)
                                      
    response = {
        "statusCode": 200,
        "body": json.dumps(result["TranslatedText"])
    }

    return response
    