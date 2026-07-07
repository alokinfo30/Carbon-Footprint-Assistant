# run.py
import os
import sys

# Add the current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    
    print("=" * 70)
    print("🌱 AI-Powered Carbon Footprint Assistant")
    print("=" * 70)
    print(f"🚀 Server running at: http://localhost:{port}")
    print(f"📱 Open in your browser")
    print("=" * 70)
    print("🤖 AI Agents:")
    print("  1. 📊 Footprint Analyst - Calculates carbon footprint")
    print("  2. 📋 Reduction Strategist - Develops reduction plans")
    print("  3. 🎯 Personalization Agent - Tailors recommendations")
    print("  4. 📚 Education Agent - Provides environmental education")
    print("  5. 📈 Tracking Agent - Tracks progress")
    print("=" * 70)
    print("🌍 Supported Languages:")
    print("  English, Hindi, Spanish, French, German, Portuguese, Chinese")
    print("=" * 70)
    print("🌱 Empowering Sustainable Living")
    print("=" * 70)
    
    app.run(host='0.0.0.0', port=port, debug=debug)