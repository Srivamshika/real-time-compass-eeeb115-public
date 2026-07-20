from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Real Time Compass', version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://[a-z0-9-]+\.vercel\.app",
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
PRODUCT = {"project_id": "eeeb1152-de16-40a3-b144-178a15e62be5", "product_name": "Real Time Compass", "idea": "Real-time enterprise security software that detects deepfakes, cloned executive voices, and altered video streams to prevent high-value corporate fraud during digital transactions.", "problem": "Risk, finance, and operations teams need a safer, faster way to make a time-sensitive financial decision with evidence and an audit trail. The opportunity should be tested through one repeatable decision workflow.", "elevator_pitch": "Real Time Compass helps risk, finance, and operations teams turn scattered evidence into a human-approved next action and prove whether the workflow improves a measurable outcome.", "target_users": ["risk, finance, and operations teams", "domain specialists", "a finance, risk, or operations leader"], "features": ["Structured case or workflow intake", "Evidence-backed recommendation with confidence and rationale", "Human approval and override with an audit trail", "Pilot dashboard for time, quality, and adoption outcomes"], "market_gap": "A narrow financial operations workflow that links evidence, a human approval, and a measurable outcome remains more defensible than another general AI chat surface."}

@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "generated-mvp-api"}

@app.get("/api/overview")
def overview() -> dict:
    return {
        "product_name": PRODUCT["product_name"],
        "pitch": PRODUCT["elevator_pitch"],
        "problem": PRODUCT["problem"],
        "target_users": PRODUCT["target_users"],
        "features": PRODUCT["features"],
        "demo_data": True,
    }
