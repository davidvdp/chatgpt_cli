from argparse import ArgumentParser
import openai

parser = ArgumentParser('ChatGPT client using OpenAI API.')
parser.add_argument(
    'key',
    help='OpenAI API key'
)
parser.add_argument(
    '--temperature',
    '-t',
    help='ChatGPT temperature parameter between 0.0 and 1.0.',
    type=float,
    default=0.5,
    )
args = parser.parse_args()

api_key = args.key
temperature = args.temperature
if temperature > 1 or temperature < 0:
    print('Temperature should be between 0.0 and 1.0.')
    exit(-1) 

openai.api_key = api_key
model_engine = "text-davinci-003"

try:
    while True:
        prompt = input('Enter your question:\n')
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        print(response)
except KeyboardInterrupt:
    pass
