import boto3
import json

content = "application/json"
accept = "application/json"

model_id = 'mistral.mistral-7b-instruct-v0:2'

client = boto3.client(
    service_name = 'bedrock-runtime',
    region_name = 'us-east-1',
    aws_access_key_id = 'AKIAV6E5X54WU7N4LG45',
    aws_secret_access_key = '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'
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

