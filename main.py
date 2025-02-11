from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Clever AI Platform API")

class LandData(BaseModel):
    id: int
    location: str
    price: float

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Clever AI Platform"}

@app.post("/land", tags=["Land Operations"])
async def create_land(data: LandData):
    # Example: Process incoming data, integrate with AI/ML models.
    return {"status": "success", "data": data}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
