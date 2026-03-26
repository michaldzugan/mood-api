from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title="Mood API", description="A simple mood tracking API")
mood_entries = []
class MoodEntry(BaseModel):
    score: int
    note: str
@app.get("/health")
def health_check():
    """Check if the API is running."""
    return {"status": "healthy"}
@app.post("/mood")
def create_mood(entry: MoodEntry):
    """Record a new mood entry."""
    mood_entries.append(entry)
    return entry
@app.get("/moods")
def get_moods():
    """Retrieve all mood entries."""
    return mood_entries
@app.get("/moods/average")
def get_average():
    """Return the average mood score."""
    if len(mood_entries) == 0:
        return {"average": None, "message": "No mood entries yet"}
    average = sum(entry.score for entry in mood_entries) / len(mood_entries)
    return {"average": round(average, 2)}
