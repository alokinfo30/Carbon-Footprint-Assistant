# app/main.py
from flask import Blueprint, render_template, request, jsonify, current_app
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
import json
import uuid
from datetime import datetime

load_dotenv()
logger = logging.getLogger(__name__)

main_bp = Blueprint('main', __name__)

# Import crew
try:
    from app.crew import CarbonFootprintCrew
    CREW_AVAILABLE = True
    logger.info("✅ CarbonFootprintCrew imported successfully")
except ImportError as e:
    logger.warning(f"⚠️ Crew not available: {e}")
    CREW_AVAILABLE = False

# Service mapping
SERVICES = {
    "analyze": {
        "name": "Carbon Footprint Analysis",
        "icon": "📊",
        "description": "Calculate your carbon footprint"
    },
    "strategies": {
        "name": "Reduction Strategies",
        "icon": "📋",
        "description": "Get personalized reduction plans"
    },
    "personalize": {
        "name": "Personalized Recommendations",
        "icon": "🎯",
        "description": "Tailored advice for your lifestyle"
    },
    "educate": {
        "name": "Environmental Education",
        "icon": "📚",
        "description": "Learn about sustainability"
    },
    "track": {
        "name": "Progress Tracking",
        "icon": "📈",
        "description": "Track your carbon reduction journey"
    }
}

SUPPORTED_LANGUAGES = os.getenv('SUPPORTED_LANGUAGES', 'en,hi,es,fr,de,pt,zh').split(',')

@main_bp.route('/')
def index():
    """Render the main page"""
    return render_template('index.html', 
                         services=SERVICES, 
                         languages=SUPPORTED_LANGUAGES)

@main_bp.route('/api/service', methods=['POST'])
def handle_service():
    """Handle a service request"""
    try:
        data = request.json
        service_type = data.get('service_type')
        
        if not service_type:
            return jsonify({
                'error': 'Missing service type',
                'status': 'error'
            }), 400
        
        if service_type not in SERVICES:
            return jsonify({
                'error': f'Invalid service type: {service_type}',
                'status': 'error'
            }), 400
        
        if not CREW_AVAILABLE:
            return jsonify({
                'error': 'CrewAI not available. Please check installation.',
                'status': 'error'
            }), 500
        
        language = data.get('language', 'en')
        crew = CarbonFootprintCrew()
        
        # Route to appropriate handler
        if service_type == 'analyze':
            activities = data.get('activities', '')
            if not activities:
                return jsonify({
                    'error': 'Missing activities for analysis',
                    'status': 'error'
                }), 400
            result = crew.analyze_footprint(activities, language)
            
        elif service_type == 'strategies':
            analysis = data.get('analysis', '')
            if not analysis:
                return jsonify({
                    'error': 'Missing analysis for strategy development',
                    'status': 'error'
                }), 400
            result = crew.develop_strategies(analysis, language)
            
        elif service_type == 'personalize':
            user_profile = data.get('user_profile', '')
            strategies = data.get('strategies', '')
            if not user_profile or not strategies:
                return jsonify({
                    'error': 'Missing user profile or strategies for personalization',
                    'status': 'error'
                }), 400
            result = crew.personalize_recommendations(user_profile, strategies, language)
            
        elif service_type == 'educate':
            topic = data.get('topic', 'sustainability')
            result = crew.educate_user(topic, language)
            
        elif service_type == 'track':
            history = data.get('history', '')
            current_status = data.get('current_status', '')
            result = crew.track_progress(history, current_status, language)
            
        else:
            return jsonify({
                'error': f'Unhandled service type: {service_type}',
                'status': 'error'
            }), 400
        
        if result['status'] == 'error':
            return jsonify({
                'error': result.get('error', 'Unknown error'),
                'status': 'error'
            }), 500
        
        return jsonify({
            'status': 'success',
            'service': service_type,
            'result': result,
            'timestamp': datetime.utcnow().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error handling service: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@main_bp.route('/api/services', methods=['GET'])
def get_services():
    """Get all available services"""
    return jsonify({
        'status': 'success',
        'services': SERVICES,
        'languages': SUPPORTED_LANGUAGES
    })

@main_bp.route('/api/models', methods=['GET'])
def get_models():
    """Get available models"""
    try:
        from app.model_manager import model_manager
        results = model_manager.test_providers()
        available = [m for m, v in results.items() if v]
        
        return jsonify({
            'status': 'success',
            'models': {
                'primary': os.getenv('OPENROUTER_PRIMARY_MODEL', 'openai/gpt-4o-mini'),
                'fallbacks': os.getenv('OPENROUTER_FALLBACK_MODELS', '').split(','),
                'available': available,
                'all_tested': results
            }
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@main_bp.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'crew_available': CREW_AVAILABLE,
        'version': '1.0.0',
        'features': list(SERVICES.keys()),
        'languages_supported': len(SUPPORTED_LANGUAGES)
    })