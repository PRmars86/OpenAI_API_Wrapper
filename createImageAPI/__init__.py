import logging
import openai
import azure.functions as func
import key

secret_key = key.secret_key

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    openai.organization = "org-azwR948N54GOXfw3iLG7nnHD"
    openai.api_key = secret_key

    req_body = req.get_json()

    output = openai.Image.create(
        prompt = req_body['prompt'],
        n = 2,
        size = "1024x1024"
    )

    output_url = output["data"][0]["url"]


    return func.HttpResponse(output_url, status_code=200)
