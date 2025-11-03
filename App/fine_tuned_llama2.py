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
    
    try:
        # 1. Define the LLM
        llm = GradientLLM(
            model="62f07e2b-c760-46c4-b512-452640dc3b63_model_adapter",
            model_kwargs=dict(max_generated_token_count=128),
        )

        # 2. Format the IPC sections as a readable string
        ipc_sections_str = ", ".join([f"Section {k}: {v}" for k, v in ipc_dict.items()])
        
        # 3. Create a simpler template
        template = """Question: Given the following FIR description: {complaint_text}

Tell me which of the following IPC sections could be applied: {ipc_sections}

Answer: """

        # 4. Create the prompt template
        prompt = PromptTemplate(
            template=template, 
            input_variables=["complaint_text", "ipc_sections"]
        )
        
        # 5. Create the chain
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        # 6. Invoke the chain
        response = chain.invoke({
            "complaint_text": complaint_text, 
            "ipc_sections": ipc_sections_str
        })

        # 7. Process the output
        response_text = response.split("Response: ", 1)[-1].strip() if "Response: " in response else response.strip()
        print("LLM Response:", response_text)
        return response_text
        
    except Exception as e:
        print(f"Error calling Gradient AI API: {str(e)}")
        # Return a fallback response based on the detected IPC sections
        fallback_response = f"Based on the FIR analysis, the following IPC sections may be applicable: {', '.join([f'Section {k}' for k in ipc_dict.keys()])}"
        return fallback_response