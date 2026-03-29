from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def root():
    return {"message": "Backend is running"}

# Risk logic
def calculate_risk(code):
    score = 0
    findings = []

    if "READ_SMS" in code:
        score += 25
        findings.append("Reads SMS")

    if "getDeviceId" in code:
        score += 20
        findings.append("Accesses Device ID")

    if "loadUrl" in code:
        score += 15
        findings.append("Loads external URLs")

    risk = "LOW"
    if score > 30:
        risk = "MEDIUM"
    if score > 60:
        risk = "HIGH"

    return score, risk, findings

# Upload endpoint
@app.post("/upload-apk")
async def upload_apk(file: UploadFile = File(...)):
    content = await file.read()
    code = content.decode(errors="ignore")[:5000]

    score, risk, findings = calculate_risk(code)

    return {
        "score": score,
        "risk": risk,
        "findings": findings
    }
