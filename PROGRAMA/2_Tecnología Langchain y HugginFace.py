from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFace
from langchain.chains import LLMChain
 
prompt = PromptTemplate(
    input_variables=["city"],
    template="¿Cómo sería un día perfecto en {city}?",
)
 
llm = HuggingFace(
          model_name="gpt-neo-2.7B", 
          temperature=0.9) 
 
llmchain = LLMChain(llm=llm, prompt=prompt)
llmchain.run("París")

response = llmchain.run("París")
#print(response["choices"])
print (response)