# app/agents.py
import os
import logging
from crewai import Agent
from app.model_manager import model_manager

logger = logging.getLogger(__name__)

try:
    from crewai_tools import SerperDevTool, ScrapeWebsiteTool
    TOOLS_AVAILABLE = True
except ImportError:
    logger.warning("⚠️ crewai_tools not available. Using fallback.")
    TOOLS_AVAILABLE = False
    
    class SerperDevTool:
        def __init__(self):
            self.name = "SerperDevTool"
            self.description = "Search tool (fallback)"
        def run(self, query):
            return f"Search results for: {query} (fallback)"
    
    class ScrapeWebsiteTool:
        def __init__(self):
            self.name = "ScrapeWebsiteTool"
            self.description = "Web scraping tool (fallback)"
        def run(self, url):
            return f"Scraped content from: {url} (fallback)"

def create_footprint_analyzer():
    """Create the footprint analyzer agent"""
    config = model_manager.get_model_config('footprint_analyzer')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.2))
    
    return Agent(
        role="Carbon Footprint Analyst",
        goal="Calculate and analyze carbon footprints based on user activities",
        backstory=(
            "You are an environmental data scientist specializing in carbon footprint "
            "analysis. You understand emission factors for various activities including "
            "transportation, energy usage, food consumption, and waste. You provide "
            "accurate calculations and meaningful insights."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm,
        tools=[SerperDevTool(), ScrapeWebsiteTool()]
    )

def create_reduction_strategist():
    """Create the reduction strategist agent"""
    config = model_manager.get_model_config('reduction_strategist')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.4))
    
    return Agent(
        role="Carbon Reduction Strategist",
        goal="Develop personalized strategies to reduce carbon footprint",
        backstory=(
            "You are a sustainability expert who helps individuals reduce their "
            "environmental impact. You understand which actions have the most significant "
            "impact and can prioritize recommendations based on effectiveness and ease "
            "of implementation."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

def create_personalization_agent():
    """Create the personalization agent"""
    config = model_manager.get_model_config('personalization_agent')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.5))
    
    return Agent(
        role="Personalization Specialist",
        goal="Tailor recommendations based on user lifestyle and preferences",
        backstory=(
            "You are a behavioral economist who understands how to motivate sustainable "
            "behavior change. You personalize recommendations based on user preferences, "
            "lifestyle, and readiness to change."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

def create_education_agent():
    """Create the education agent"""
    config = model_manager.get_model_config('education_agent')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.6))
    
    return Agent(
        role="Environmental Education Specialist",
        goal="Educate users about environmental impact and sustainable living",
        backstory=(
            "You are an environmental educator who explains complex environmental "
            "concepts in simple, engaging terms. You help users understand why their "
            "actions matter and how they contribute to a sustainable future."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

def create_tracking_agent():
    """Create the tracking agent"""
    config = model_manager.get_model_config('tracking_agent')
    llm = model_manager.get_llm(config['model'], config.get('temperature', 0.3))
    
    return Agent(
        role="Progress Tracking Specialist",
        goal="Track and visualize carbon reduction progress over time",
        backstory=(
            "You are a data visualization expert who helps users track their progress. "
            "You create clear, motivating visualizations and reports that show how "
            "users are reducing their carbon footprint."
        ),
        allow_delegation=False,
        verbose=True,
        llm=llm
    )