from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import GradientLLM

import os
from getpass import getpass

if not os.environ.get("GRADIENT_ACCESS_TOKEN", None):
    # Access token under https://auth.gradient.ai/select-workspace
    os.environ["GRADIENT_ACCESS_TOKEN"] = "smX00wSAmvAZSJLLUhkVOqf0UYhdStj3"
if not os.environ.get("GRADIENT_WORKSPACE_ID", None):
    # `ID` listed in `$ gradient workspace list`
    # also displayed after login at at https://auth.gradient.ai/select-workspace
    os.environ["GRADIENT_WORKSPACE_ID"] = "880ee27e-5b8f-4057-a266-209896ce267c_workspace"

if not os.environ.get("GRADIENT_API_URL", None):
    os.environ["GRADIENT_API_URL"] = "https://auth.gradient.ai/api"


def generate_query(complaint_text, ipc_dict):
    print(complaint_text)

    # 1. Define the LLM
    llm = GradientLLM(
        model="62f07e2b-c760-46c4-b512-452640dc3b63_model_adapter",
        model_kwargs=dict(max_generated_token_count=128),
    )

    # 2. Define the template with the *actual* input variables
    template = """Question: Given the following FIR description, {complaint_text}
    Tell me which of the following IPC sections could be applied: {ipc_dict}
    Answer: """

    # 3. Create the prompt template
    prompt = PromptTemplate(
        template=template, 
        input_variables=[complaint_text, ipc_dict]  # Use the real variables
    )
    
    # 4. Create the chain
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # 5. Invoke the chain with the original inputs
    response = chain.invoke({
        "complaint_text": complaint_text, 
        "ipc_dict": ipc_dict
    })

    # 6. Process the output
    response_text = response.split("Response: ", 1)[-1].strip()
    print(response_text)
    return response_text