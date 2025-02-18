import json
import requests

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = 'mistral:7b-instruct-v0.2-q8_0' # chosen LLM model specified here

def generate(prompt, context):
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        # the response streams one token at a time, print that as we receive it
        print(response_part, end='', flush=True)

        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return body['context']

def main():
    context = [] # the context stores a conversation history, you can use this to make the model more context aware
    user_input = "generate more basic programming problems/challenges together with unit tests for their solutions' verification"
    print(user_input)
    context = generate(user_input, context)
    print()

if __name__ == "__main__":
    main()
