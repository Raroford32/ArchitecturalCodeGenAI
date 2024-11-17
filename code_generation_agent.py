from utils.llm_client import LLMClient
from utils.memory_store import MemoryStore
import os
import json

class CodeGenerationAgent:
    def __init__(self):
        self.llm_client = LLMClient()
        self.memory_store = MemoryStore()
        self.output_dir = 'output/src'

    def generate_code(self):
        architecture_json = self.memory_store.retrieve('architecture')
        architecture = json.loads(architecture_json)
        components = architecture.get('modules', [])
        os.makedirs(self.output_dir, exist_ok=True)
        for component in components:
            self.generate_component_code(component)

    def generate_component_code(self, component):
        prompt = (
            f"You are a senior software developer. Write the complete source code for the following module.\n\n"
            f"Module Name: {component['name']}\n"
            f"Description: {component['description']}\n"
            f"Dependencies: {', '.join(component.get('dependencies', []))}\n\n"
            "Ensure the code is well-documented with comments, follows best practices, and includes necessary imports. "
            "Provide the code in Python, and do not include any explanations or additional text."
        )
        code = self.llm_client.generate_response(prompt)
        file_name = component['file_name']
        file_path = os.path.join(self.output_dir, file_name)
        with open(file_path, 'w') as file:
            file.write(code)
        self.memory_store.save(f'code_{component["name"]}', code)
