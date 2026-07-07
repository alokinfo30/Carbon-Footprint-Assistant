# Carbon-Footprint-Assistant
AI-powered Carbon Footprint Assistant that helps individuals understand, track, and reduce their carbon footprint through personalized insights.


CarbonFootprintAssistant/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model_manager.py
│   ├── agents.py
│   ├── tasks.py
│   ├── crew.py
│   ├── models.py
│   └── utils.py
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
├── data/
│   └── .gitkeep
├── .env
├── .gitignore
├── requirements.txt
├── run.py
└── README.md



# 🌱 AI-Powered Carbon Footprint Assistant

An intelligent assistant that helps individuals understand, track, and reduce their carbon footprint through simple actions and personalized insights.

## Features

- 📊 **Carbon Footprint Analysis**: Calculate your carbon footprint based on daily activities
- 📋 **Reduction Strategies**: Get personalized plans to reduce your impact
- 🎯 **Personalized Recommendations**: Tailored advice for your lifestyle
- 📚 **Environmental Education**: Learn about sustainability topics
- 📈 **Progress Tracking**: Track your carbon reduction journey
- 🌍 **Multi-Language Support**: 7+ languages available

## Architecture

### AI Agents

1. **Footprint Analyst**: Calculates and analyzes carbon footprints
2. **Reduction Strategist**: Develops personalized reduction strategies
3. **Personalization Agent**: Tailors recommendations to user preferences
4. **Education Agent**: Provides environmental education content
5. **Tracking Agent**: Tracks and visualizes progress

### Technology Stack

- **CrewAI** - Multi-agent orchestration
- **OpenRouter** - Multi-model support with auto-fallback
- **Flask** - Web framework
- **Pydantic** - Data validation
- **HTML/CSS/JS** - Responsive frontend

### Models Used

| Model | Provider | Use Case |
|-------|----------|----------|
| `openai/gpt-4o-mini` | OpenAI | Footprint Analysis, Tracking |
| `mistralai/mixtral-8x22b-instruct` | Mistral | Reduction Strategies |
| `meta-llama/llama-3.1-8b-instruct` | Meta | Personalization |
| `deepseek/deepseek-chat` | DeepSeek | Education |

## Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd CarbonFootprintAssistant

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file with your OpenRouter API key
# (see .env.example for template)

# 5. Run the application
python run.py




Configuration
Environment Variables
Variable	Description
OPENROUTER_API_KEY	Your OpenRouter API key
OPENROUTER_PRIMARY_MODEL	Primary model to use
OPENROUTER_FALLBACK_MODELS	Fallback models
SUPPORTED_LANGUAGES	Comma-separated language codes
API Endpoints
Endpoint	Method	Description
/	GET	Web interface
/api/service	POST	Handle service request
/api/services	GET	List all services
/api/models	GET	List available models
/api/health	GET	Health check
Service Types
analyze - Carbon footprint analysis

strategies - Reduction strategies

personalize - Personalized recommendations

educate - Environmental education

track - Progress tracking




✅ Features:
5 Specialized AI Agents for different carbon services

7+ Languages support for diverse users

Interactive Interface for easy understanding

Auto-Fallback between 4 different models

Responsive Design for mobile and desktop

Export and Copy functionality

Real-time Status Updates during processing

✅ Services:
📊 Carbon Footprint Analysis - Calculate your impact

📋 Reduction Strategies - Get personalized plans

🎯 Personalized Recommendations - Tailored advice

📚 Environmental Education - Learn about sustainability

📈 Progress Tracking - Monitor your journey

✅ Technology Stack:
CrewAI for multi-agent orchestration

OpenRouter for multi-model support

Flask for web interface

Pydantic for data validation






