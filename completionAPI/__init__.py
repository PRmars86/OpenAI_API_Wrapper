import logging

import azure.functions as func
import openai
import key

secret_key = key.secret_key

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    openai.organization = "org-azwR948N54GOXfw3iLG7nnHD"
    openai.api_key = secret_key

    req_body = req.get_json()

    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    )

    output_text = output['choices'][0]['text']

    return func.HttpResponse(output_text, status_code=200)

    