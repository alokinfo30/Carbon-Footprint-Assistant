# app/tasks.py
from crewai import Task
import logging

logger = logging.getLogger(__name__)

def create_analyze_footprint_task(agent, activities: str, language: str = "en"):
    """Create the footprint analysis task"""
    return Task(
        description=f"""
        Calculate and analyze the carbon footprint for the following activities:
        
        User Activities:
        {activities}
        
        Calculate carbon emissions for:
        1. Transportation (vehicle type, distance, frequency)
        2. Energy usage (electricity, heating, cooling)
        3. Food consumption (diet type, food waste)
        4. Waste management (recycling, landfill waste)
        5. Shopping habits (new purchases, second-hand items)
        
        Provide:
        - Total carbon footprint in kg CO2e per year
        - Breakdown by category
        - Comparison to national/global averages
        - Key insights about the user's footprint
        
        Language: {language}
        """,
        expected_output="""
        A comprehensive carbon footprint analysis report with numerical values 
        and actionable insights.
        """,
        agent=agent
    )

def create_develop_strategies_task(agent, analysis: str, language: str = "en"):
    """Create the reduction strategies task"""
    return Task(
        description=f"""
        Develop personalized carbon reduction strategies based on the user's footprint:
        
        User Footprint Analysis:
        {analysis}
        
        Create strategies that:
        1. Prioritize actions with highest impact
        2. Consider ease of implementation
        3. Provide estimated carbon savings
        4. Include timeline recommendations
        5. Suggest behavioral changes
        
        Include specific, actionable steps the user can take.
        Language: {language}
        """,
        expected_output="""
        A detailed action plan with prioritized strategies and estimated impact.
        """,
        agent=agent
    )

def create_personalize_recommendations_task(agent, user_profile: str, strategies: str, language: str = "en"):
    """Create the personalization task"""
    return Task(
        description=f"""
        Personalize recommendations based on user preferences:
        
        User Profile:
        {user_profile}
        
        Strategies to personalize:
        {strategies}
        
        Tailor the recommendations by considering:
        1. User lifestyle and daily routine
        2. Budget constraints
        3. Motivation level and readiness to change
        4. Location and available resources
        5. Personal values and interests
        
        Make the recommendations feel achievable and motivating.
        Language: {language}
        """,
        expected_output="""
        Personalized recommendations with implementation guidance.
        """,
        agent=agent
    )

def create_educate_user_task(agent, topic: str, language: str = "en"):
    """Create the education task"""
    return Task(
        description=f"""
        Create educational content about environmental impact:
        
        Topic: {topic}
        
        Create engaging content that:
        1. Explains the environmental issue in simple terms
        2. Connects to the user's daily activities
        3. Provides practical tips and actions
        4. Includes fun facts and statistics
        5. Motivates behavior change
        
        Format the content to be easy to understand and shareable.
        Language: {language}
        """,
        expected_output="""
        Engaging educational content about environmental sustainability.
        """,
        agent=agent
    )

def create_track_progress_task(agent, history: str, current_status: str, language: str = "en"):
    """Create the progress tracking task"""
    return Task(
        description=f"""
        Track and visualize carbon reduction progress:
        
        Historical Data:
        {history}
        
        Current Status:
        {current_status}
        
        Create:
        1. Progress visualization recommendations
        2. Achievement milestones
        3. Comparison to goals
        4. Motivation and encouragement
        5. Next steps and challenges
        
        Make the progress tracking motivating and engaging.
        Language: {language}
        """,
        expected_output="""
        A progress tracking report with visualizations and motivation.
        """,
        agent=agent
    )