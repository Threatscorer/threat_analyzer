from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/upload-apk")
async def upload_apk(file: UploadFile):
    content = await file.read()

    return {
        "score": 85,
        "risk": "Medium",
        "findings": ["Suspicious permission", "External API call"]
    }
