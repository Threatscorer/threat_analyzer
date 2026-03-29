from fastapi import FastAPI, UploadFile, File
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

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
    if score > 30: risk = "MEDIUM"
    if score > 60: risk = "HIGH"

    return {"score": score, "risk": risk, "findings": findings}


@app.post("/chat")
async def chat(prompt: str):
    response = requests.post(OLLAMA_URL, json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    return {"response": response.json()["response"]}


@app.post("/upload-apk")
async def upload_apk(file: UploadFile = File(...)):
    content = await file.read()
    code = content.decode(errors="ignore")[:5000]

    risk = calculate_risk(code)

    return {
        "message": "Analysis complete",
        "risk": risk
    }
