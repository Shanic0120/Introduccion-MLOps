from pydantic import BaseModel

class PredictionRequest(BaseModel):
    Age: int
    Gender: int
    EducationLevel: int
    ExperienceYears: int
    PreviousCompanies: int
    DistanceFromCompany: float
    InterviewScore: int
    SkillScore: int
    PersonalityScore: int
    RecruitmentStrategy: int
    

class PredictionResponse(BaseModel):
    HiringDecision: int