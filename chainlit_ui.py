import chainlit as cl
from agents.requirement_analysis_agent import RequirementAnalysisAgent
from agents.architectural_design_agent import ArchitecturalDesignAgent
from agents.code_generation_agent import CodeGenerationAgent
from agents.integration_agent import IntegrationAgent
from agents.memory_management_agent import MemoryManagementAgent

requirement_agent = RequirementAnalysisAgent()
architecture_agent = ArchitecturalDesignAgent()
code_gen_agent = CodeGenerationAgent()
integration_agent = IntegrationAgent()

@cl.on_message
def handle_message(message: str):
    # Step 1: Gather requirements from the user
    detailed_requirements = requirement_agent.gather_requirements(message)
    cl.Message(content=detailed_requirements).send()

    # Step 2: Create architectural design based on requirements
    architecture_json = architecture_agent.create_architecture()
    cl.Message(content="Architecture designed successfully!").send()

    # Step 3: Generate code based on the architecture
    code_gen_agent.generate_code()
    cl.Message(content="Code generation completed!").send()

    # Step 4: Integrate the generated code into a single build
    integration_agent.integrate_code()
    cl.Message(content="Code integration completed!").send()
