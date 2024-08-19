import boto3
import io
import json
import base64

from PIL import Image


def main():

    bedrock_client = boto3.client(service_name="bedrock-runtime", region_name="us-east-1", 
                                  aws_access_key_id="AWS Access key id",
                                  aws_secret_access_key ="AWS secret key id"
                                  )
    accept = "application/json"
    content_type = "application/json"
    model_id = "stability.stable-diffusion-xl-v1"

    prompt = "Sri Lanks tea plantation"

    body = json.dumps({
        "text_prompts": [
            {
                "text" : prompt
            }
        ],
        "cfg_scle": 10,
        "seed": 0
    })


    response = bedrock_client.invoke_model(
        body=body, modelId = model_id, contentType =content_type, accept = accept
    )

    response_body = json.loads(response.get('body').read())

    base64_image = response_body.get("artifacts")[0].get('base64')
    base_bytes = base64_image.encode("ascii")
    image_bytes = base64.b64decode(base_bytes)


    image = Image.open(io.BytesIO(image_bytes))
    image.show()

if __name__ == "__main__":
    main()


