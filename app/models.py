# app/models.py
from pydantic import BaseModel, Field
from typing import Dict, Optional, List, Any
from datetime import datetime
from enum import Enum

class ActivityType(str, Enum):
    """Types of carbon-emitting activities"""
    TRANSPORTATION = "transportation"
    ENERGY = "energy"
    FOOD = "food"
    WASTE = "waste"
    SHOPPING = "shopping"

class CarbonActivity(BaseModel):
    """A single carbon-emitting activity"""
    type: ActivityType = Field(..., description="Activity type")
    name: str = Field(..., description="Activity name")
    description: str = Field(..., description="Activity description")
    frequency: str = Field(..., description="Frequency: daily, weekly, monthly, yearly")
    quantity: float = Field(..., description="Quantity per occurrence")
    unit: str = Field(..., description="Unit of measurement")
    emission_factor: float = Field(..., description="CO2e per unit")

class CarbonFootprint(BaseModel):
    """Complete carbon footprint analysis"""
    total_emissions: float = Field(..., description="Total CO2e in kg per year")
    breakdown: Dict[str, float] = Field(..., description="Emissions by category")
    comparison: Dict[str, str] = Field(..., description="Comparison to averages")
    insights: List[str] = Field(..., description="Key insights")
    potential_savings: Dict[str, float] = Field(..., description="Potential savings by action")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

class ReductionStrategy(BaseModel):
    """A carbon reduction strategy"""
    id: str = Field(..., description="Strategy identifier")
    category: str = Field(..., description="Strategy category")
    action: str = Field(..., description="Action to take")
    description: str = Field(..., description="Detailed description")
    estimated_savings: float = Field(..., description="Estimated CO2e savings per year")
    difficulty: str = Field(..., description="Difficulty: easy, medium, hard")
    timeframe: str = Field(..., description="Timeframe: immediate, short-term, long-term")
    cost_savings: float = Field(..., description="Estimated cost savings per year")
    steps: List[str] = Field(..., description="Implementation steps")

class PersonalizedRecommendation(BaseModel):
    """Personalized recommendation"""
    id: str = Field(..., description="Recommendation identifier")
    strategy: ReductionStrategy = Field(..., description="Base strategy")
    personalization_notes: str = Field(..., description="Personalization details")
    motivation_tips: List[str] = Field(..., description="Motivation tips")
    progress_tracking: Dict[str, Any] = Field(..., description="Progress tracking metrics")
    next_steps: List[str] = Field(..., description="Next steps")

class EducationalContent(BaseModel):
    """Educational content"""
    id: str = Field(..., description="Content identifier")
    title: str = Field(..., description="Content title")
    category: str = Field(..., description="Content category")
    summary: str = Field(..., description="Content summary")
    detailed_content: str = Field(..., description="Detailed content")
    key_takeaways: List[str] = Field(..., description="Key takeaways")
    actions: List[str] = Field(..., description="Actions to take")
    fun_facts: List[str] = Field(..., description="Fun facts")
    resources: List[str] = Field(..., description="Additional resources")

class ProgressReport(BaseModel):
    """Progress tracking report"""
    period: str = Field(..., description="Reporting period")
    current_footprint: float = Field(..., description="Current carbon footprint")
    previous_footprint: float = Field(..., description="Previous carbon footprint")
    reduction: float = Field(..., description="Total reduction achieved")
    achievements: List[str] = Field(..., description="Achievements")
    challenges: List[str] = Field(..., description="Challenges faced")
    next_goals: List[str] = Field(..., description="Next goals")
    motivation: str = Field(..., description="Motivational message")
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

class UserProfile(BaseModel):
    """User profile for personalization"""
    id: str = Field(..., description="User identifier")
    name: str = Field(..., description="User name")
    location: str = Field(..., description="User location")
    lifestyle: str = Field(..., description="Lifestyle description")
    budget_conscious: bool = Field(True, description="Is budget conscious")
    motivation_level: int = Field(..., ge=1, le=10, description="Motivation level 1-10")
    interests: List[str] = Field(..., description="User interests")
    readiness: str = Field(..., description="Readiness to change: low, medium, high")