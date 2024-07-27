import langchain
import langchain_community

print(langchain.__version__)
print(langchain_community.__version__)

import boto3
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Bedrock


## Uncomment and add your key 
aws_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
   aws_access_key_id ="YOUR KEY ID",
    aws_secret_access_key = "YOUR SECRETE KEY"
)


model_id = "mistral.mistral-7b-instruct-v0:2"


model_kwargs = {
    "max_tokens": 2048,
    "temperature": 0.5,
    "top_k" : 50,
    "top_p": 0.9
}



model = Bedrock(client = aws_client, model_id= model_id, model_kwargs = model_kwargs, streaming=False)


template = "<s> [INST] {question} [/INST]"


prompt = PromptTemplate.from_template(template)

chain = prompt | model | StrOutputParser()

response = chain.invoke({"question": "tell me a joke" })


print(response)

