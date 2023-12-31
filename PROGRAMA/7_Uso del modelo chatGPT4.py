
from openai import OpenAI

client = OpenAI(
  api_key=os.environ['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'],  # this is also the default, it can be omitted
)

completion = openai.ChatCompletion.create(
    model="gpt-4", 
    messages=[
        {"roles":"system","content": "Eres un asistente de ayuda"},
        {"roles":"user","content": "¿Puedes decirme algo que inspire a la audiencia del microsoft build 2023?"},
        ])
print(completion.choices[0].message.content)
response=completion
print(response["choices"][0]["message"]["content"])


