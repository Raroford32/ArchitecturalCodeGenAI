from utils.llm_client import LLMClient
from utils.memory_store import MemoryStore

class RequirementAnalysisAgent:
    def __init__(self):
        self.llm_client = LLMClient()
        self.memory_store = MemoryStore()

    def gather_requirements(self, user_input):
        prompt = (
            "You are an expert software analyst. Analyze the following user requirements in detail, "
            "identify any ambiguities or missing information, and provide a comprehensive and clear "
            "requirements document:\n\n"
            f"{user_input}\n\n"
            "Please structure the requirements document with numbered sections and subsections."
        )
        detailed_requirements = self.llm_client.generate_response(prompt)
        self.memory_store.save('requirements', detailed_requirements)
        return detailed_requirements
