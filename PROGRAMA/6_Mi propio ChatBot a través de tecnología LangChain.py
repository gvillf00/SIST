from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import openai
import gradio as gr
import sys
import os

openai.api_key="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"
#os.environ["OPENAI_API_KEY"] = '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'

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=openai(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Introduce tu texto"),
                     outputs="text",
                     title="Mi AI Chatbot")

index = construct_index("docs")
iface.launch(share=True)