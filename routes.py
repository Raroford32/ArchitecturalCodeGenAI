from flask import Blueprint, render_template, request, jsonify
from agents.requirement_analysis_agent import RequirementAnalysisAgent
from agents.architectural_design_agent import ArchitecturalDesignAgent
from agents.code_generation_agent import CodeGenerationAgent
from agents.integration_agent import IntegrationAgent
from agents.memory_management_agent import MemoryManagementAgent

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/generate', methods=['POST'])
def generate_code():
    try:
        requirements = request.form.get('requirements')
        if not requirements:
            return jsonify({'error': 'No requirements provided'}), 400

        # Initialize agents
        memory_agent = MemoryManagementAgent()
        req_agent = RequirementAnalysisAgent()
        arch_agent = ArchitecturalDesignAgent()
        code_agent = CodeGenerationAgent()
        integration_agent = IntegrationAgent()

        # Clear previous data
        memory_agent.clear_all_data()

        # Process requirements
        detailed_requirements = req_agent.gather_requirements(requirements)
        
        # Create architecture
        architecture = arch_agent.create_architecture()
        
        # Generate code
        code_agent.generate_code()
        
        # Integrate code
        integration_agent.integrate_code()

        return jsonify({
            'status': 'success',
            'requirements': detailed_requirements,
            'architecture': architecture,
            'message': 'Code generated successfully'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='Page not found'), 404

@main_bp.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='Internal server error'), 500
