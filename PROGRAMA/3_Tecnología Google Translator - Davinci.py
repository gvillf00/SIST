import os
import openai
import googletrans
key = "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"
translator = googletrans.Translator()
sample_text_it = "¿Cuanto tiempo se necesita para aprender Aleman?"
translated = translator.translate(sample_text_it, src='es', dest='en')
openai.api_key = key
response = openai.Completion.create(
  engine="davinci",
  prompt=translated.text,
  temperature=0.25,
  max_tokens=30,
  top_p=1
)
print(response["choices"])