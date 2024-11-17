from agents.requirement_analysis_agent import RequirementAnalysisAgent
from agents.architectural_design_agent import ArchitecturalDesignAgent
from agents.code_generation_agent import CodeGenerationAgent
from agents.integration_agent import IntegrationAgent
from agents.memory_management_agent import MemoryManagementAgent

def main():
    # Initialize Agents
    memory_agent = MemoryManagementAgent()
    memory_agent.clear_all_data()
    req_agent = RequirementAnalysisAgent()
    arch_agent = ArchitecturalDesignAgent()
    code_agent = CodeGenerationAgent()
    integration_agent = IntegrationAgent()

    # Step 1: Gather Requirements
    user_input = input("Enter your software requirements:\n")
    print("Analyzing your requirements...")
    detailed_requirements = req_agent.gather_requirements(user_input)
    print("Requirements document generated.\n")

    # Step 2: Create Architecture
    print("Designing software architecture...")
    try:
        architecture = arch_agent.create_architecture()
        print("Architecture design completed.\n")
    except ValueError as e:
        print(f"Error in architecture design: {e}")
        return

    # Step 3: Generate Code
    print("Generating source code for components...")
    code_agent.generate_code()
    print("Code generation completed.\n")

    # Step 4: Integrate Code
    print("Integrating code components...")
    integration_agent.integrate_code()
    print("Code integration completed.\n")

    # Final Output
    print("The source code has been generated and integrated successfully.")
    print("You can find the source files in the 'output/src' directory and the integrated build in the 'output/build' directory.")

if __name__ == '__main__':
    main()
