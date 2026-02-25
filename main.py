from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ResumeData(BaseModel):
    user_id: str
    name: str
    email: str
    skills: List[str]
    education: list
    projects: list
    experience: list
    raw_text: str

@app.post("/score")
def score_resume(data: ResumeData):

    # Dummy scoring (replace with real ML later)
    skill_score = min(len(data.skills) * 10, 100)
    experience_score = 70
    project_score = 80
    education_score = 75
    ats_score = 85

    final_score = (
        0.30 * skill_score +
        0.25 * experience_score +
        0.20 * project_score +
        0.15 * education_score +
        0.10 * ats_score
    )

    return {
        "skill_score": skill_score,
        "experience_score": experience_score,
        "project_score": project_score,
        "education_score": education_score,
        "ats_score": ats_score,
        "final_score": round(final_score, 2),
        "suggestions": [
            "Add more quantified achievements",
            "Improve formatting for ATS"
        ]
    }