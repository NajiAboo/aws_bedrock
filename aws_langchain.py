import langchain
import langchain_community

print(langchain.__version__)
print(langchain_community.__version__)

import boto3
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Bedrock


aws_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
    aws_access_key_id ="AKIAV6E5X54W6XKSEAWS",
    aws_secret_access_key = "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"
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

