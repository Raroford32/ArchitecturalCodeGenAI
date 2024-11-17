from utils.llm_client import LLMClient
from utils.memory_store import MemoryStore
import json
import re

class ArchitecturalDesignAgent:
    def __init__(self):
        self.llm_client = LLMClient()
        self.memory_store = MemoryStore()

    def create_architecture(self):
        requirements = self.memory_store.retrieve('requirements')
        prompt = (
            "You are a seasoned software architect. Based on the following requirements, design a detailed "
            "software architecture. Include the following:\n"
            "- Overall system architecture diagram (describe in text)\n"
            "- List of modules/classes with their responsibilities\n"
            "- File structure and relationships between components\n\n"
            "Requirements:\n"
            f"{requirements}\n\n"
            "Provide the architecture in JSON format with the following structure:\n"
            "{\n"
            "  'modules': [\n"
            "    {\n"
            "      'name': 'ModuleName',\n"
            "      'description': 'Description of the module',\n"
            "      'file_name': 'module_name.py',\n"
            "      'dependencies': ['DependencyModule1', 'DependencyModule2']\n"
            "    },\n"
            "    ...\n"
            "  ]\n"
            "}"
        )
        architecture = self.llm_client.generate_response(prompt)
        # Clean up the JSON response
        architecture_json = self.clean_json_response(architecture)
        self.memory_store.save('architecture', architecture_json)
        return architecture_json

    def clean_json_response(self, response):
        # Extract JSON content from the response
        json_str = re.search(r'\{.*\}', response, re.DOTALL)
        if json_str:
            json_str = json_str.group(0)
            try:
                architecture = json.loads(json_str)
                return json.dumps(architecture, indent=2)
            except json.JSONDecodeError:
                raise ValueError("Failed to parse architecture JSON.")
        else:
            raise ValueError("No JSON content found in the response.")