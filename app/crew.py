# app/crew.py
from crewai import Crew
import os
import logging
from typing import Dict, List, Optional
from app.model_manager import model_manager

logger = logging.getLogger(__name__)

class CarbonFootprintCrew:
    """Orchestrate the carbon footprint assistant services"""
    
    def __init__(self):
        try:
            from app.agents import (
                create_footprint_analyzer,
                create_reduction_strategist,
                create_personalization_agent,
                create_education_agent,
                create_tracking_agent
            )
            from app.tasks import (
                create_analyze_footprint_task,
                create_develop_strategies_task,
                create_personalize_recommendations_task,
                create_educate_user_task,
                create_track_progress_task
            )
            
            self.create_footprint_analyzer = create_footprint_analyzer
            self.create_reduction_strategist = create_reduction_strategist
            self.create_personalization_agent = create_personalization_agent
            self.create_education_agent = create_education_agent
            self.create_tracking_agent = create_tracking_agent
            
            self.create_analyze_footprint_task = create_analyze_footprint_task
            self.create_develop_strategies_task = create_develop_strategies_task
            self.create_personalize_recommendations_task = create_personalize_recommendations_task
            self.create_educate_user_task = create_educate_user_task
            self.create_track_progress_task = create_track_progress_task
            
            self.verbose = os.getenv('DEBUG', 'False').lower() == 'true'
            self.model_manager = model_manager
            
            logger.info("✅ CarbonFootprintCrew initialized")
            
        except Exception as e:
            logger.error(f"Failed to initialize CarbonFootprintCrew: {str(e)}")
            raise
    
    def analyze_footprint(self, activities: str, language: str = "en") -> Dict:
        """Analyze carbon footprint"""
        try:
            logger.info(f"📊 Analyzing carbon footprint")
            
            agent = self.create_footprint_analyzer()
            task = self.create_analyze_footprint_task(agent, activities, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "activities": activities,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "footprint_analysis",
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Footprint analysis failed: {str(e)}")
            return {
                "status": "error",
                "service": "footprint_analysis",
                "error": str(e)
            }
    
    def develop_strategies(self, analysis: str, language: str = "en") -> Dict:
        """Develop reduction strategies"""
        try:
            logger.info(f"📋 Developing reduction strategies")
            
            agent = self.create_reduction_strategist()
            task = self.create_develop_strategies_task(agent, analysis, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "analysis": analysis,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "reduction_strategies",
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Strategy development failed: {str(e)}")
            return {
                "status": "error",
                "service": "reduction_strategies",
                "error": str(e)
            }
    
    def personalize_recommendations(self, user_profile: str, strategies: str, language: str = "en") -> Dict:
        """Personalize recommendations"""
        try:
            logger.info(f"🎯 Personalizing recommendations")
            
            agent = self.create_personalization_agent()
            task = self.create_personalize_recommendations_task(
                agent, user_profile, strategies, language
            )
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "user_profile": user_profile,
                "strategies": strategies,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "personalization",
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Personalization failed: {str(e)}")
            return {
                "status": "error",
                "service": "personalization",
                "error": str(e)
            }
    
    def educate_user(self, topic: str, language: str = "en") -> Dict:
        """Educate user about environmental topics"""
        try:
            logger.info(f"📚 Creating educational content about: {topic}")
            
            agent = self.create_education_agent()
            task = self.create_educate_user_task(agent, topic, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "topic": topic,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "education",
                "language": language,
                "topic": topic,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Education failed: {str(e)}")
            return {
                "status": "error",
                "service": "education",
                "error": str(e)
            }
    
    def track_progress(self, history: str, current_status: str, language: str = "en") -> Dict:
        """Track progress"""
        try:
            logger.info(f"📈 Tracking progress")
            
            agent = self.create_tracking_agent()
            task = self.create_track_progress_task(agent, history, current_status, language)
            
            crew = Crew(agents=[agent], tasks=[task], verbose=self.verbose)
            result = crew.kickoff(inputs={
                "history": history,
                "current_status": current_status,
                "language": language
            })
            
            return {
                "status": "success",
                "service": "progress_tracking",
                "language": language,
                "result": str(result)
            }
            
        except Exception as e:
            logger.error(f"Progress tracking failed: {str(e)}")
            return {
                "status": "error",
                "service": "progress_tracking",
                "error": str(e)
            }