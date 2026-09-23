from fastapi import FastAPI

app = FastAPI(
    title="Techlog Solutions API",
    description="CRM para techlog Solutions",
    version="1.0.0"
)

@app.get("/")
async def health_check():
    return {"Status": "OK"}