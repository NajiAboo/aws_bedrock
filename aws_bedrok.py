import boto3
import json


content = "application/json"
accept = "application/json"

model_id = 'mistral.mistral-7b-instruct-v0:2'

#uncomment the aws_access_key_id and aws_secret_access_key and add your keys
client = boto3.client(
    service_name = 'bedrock-runtime',
    region_name = 'us-east-1',
    #aws_access_key_id = 'Your ACCESS KEY',
    #aws_secret_access_key = 'Your SECRETE KEY'
)

prompt = "Describe about aWS bedrock in a single sentence"

format_prompt = f'<s>[INST] {prompt} [/INST]'

request_config = {
    'temperature' : 0.5,
    'prompt' : format_prompt,
    'max_tokens' : 512
}

body = json.dumps(request_config)


response = client.invoke_model (
    modelId = model_id, 
    body=body,
    accept=accept,
    contentType =content
)

#print(response)

if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    result = response.get('body').read()
    print(json.loads(result)['outputs'][0]['text'])

