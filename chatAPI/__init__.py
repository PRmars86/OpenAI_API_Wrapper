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
    model = "gpt-3.5-turbo"

    output = openai.ChatCompletion.create(
        model = model,
        messages=[
        {"role": "system", "content": req_body['prompt']},
    ],
        max_tokens = 500,
        temperature = 0
    )

    output_text = output['choices'][0]['message']['content']

    return func.HttpResponse(output_text, status_code=200)
