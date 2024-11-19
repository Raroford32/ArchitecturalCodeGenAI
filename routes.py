from flask import Blueprint, render_template, request, jsonify
import logging
import traceback
from agents.requirement_analysis_agent import RequirementAnalysisAgent
from agents.architectural_design_agent import ArchitecturalDesignAgent
from agents.code_generation_agent import CodeGenerationAgent
from agents.integration_agent import IntegrationAgent
from agents.memory_management_agent import MemoryManagementAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/generate', methods=['POST'])
def generate_code():
    try:
        # Input validation
        requirements = request.form.get('requirements')
        project_name = request.form.get('projectName')
        
        if not requirements or not requirements.strip():
            return jsonify({'error': 'No requirements provided'}), 400
        if not project_name or not project_name.strip():
            return jsonify({'error': 'No project name provided'}), 400

        # Initialize agents with error handling
        try:
            memory_agent = MemoryManagementAgent()
            req_agent = RequirementAnalysisAgent()
            arch_agent = ArchitecturalDesignAgent()
            code_agent = CodeGenerationAgent(project_name=project_name)
            integration_agent = IntegrationAgent()
        except Exception as e:
            logger.error(f"Agent initialization failed: {str(e)}\n{traceback.format_exc()}")
            return jsonify({'error': f'Failed to initialize agents: {str(e)}'}), 500

        # Clear previous data with error handling
        try:
            memory_agent.clear_all_data()
        except Exception as e:
            logger.error(f"Clear data failed: {str(e)}\n{traceback.format_exc()}")
            return jsonify({'error': f'Failed to clear previous data: {str(e)}'}), 500

        # Process requirements with error handling
        try:
            detailed_requirements = req_agent.gather_requirements(requirements)
            if not detailed_requirements:
                raise ValueError("Failed to generate detailed requirements")
        except Exception as e:
            logger.error(f"Requirements processing failed: {str(e)}\n{traceback.format_exc()}")
            return jsonify({'error': f'Failed to process requirements: {str(e)}'}), 500

        # Create architecture with error handling
        try:
            architecture = arch_agent.create_architecture()
            if not architecture:
                raise ValueError("Failed to generate architecture")
        except Exception as e:
            logger.error(f"Architecture creation failed: {str(e)}\n{traceback.format_exc()}")
            return jsonify({'error': f'Failed to create architecture: {str(e)}'}), 500

        # Generate code with error handling
        try:
            code_agent.generate_code()
        except Exception as e:
            logger.error(f"Code generation failed: {str(e)}\n{traceback.format_exc()}")
            return jsonify({'error': f'Failed to generate code: {str(e)}'}), 500

        # Integrate code with error handling
        try:
            integration_agent.integrate_code()
        except Exception as e:
            logger.error(f"Code integration failed: {str(e)}\n{traceback.format_exc()}")
            return jsonify({'error': f'Failed to integrate code: {str(e)}'}), 500

        # Return success response with proper content type
        response = jsonify({
            'status': 'success',
            'requirements': detailed_requirements,
            'architecture': architecture,
            'message': f'Code generated successfully in output/{project_name}/src directory'
        })
        response.headers['Content-Type'] = 'application/json'
        return response

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}\n{traceback.format_exc()}")
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@main_bp.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error='Page not found'), 404

@main_bp.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='Internal server error'), 500
