from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from src.DocSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, text: str = Form(...)):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return templates.TemplateResponse("index.html", {"request": request, "result": summary, "input_text": text})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "result": f"Error: {e}"})


@app.get("/train", response_class=HTMLResponse)
async def training(request: Request):
    try:
        os.system("python main.py")
        return templates.TemplateResponse("index.html", {"request": request, "train_msg": "✅ Training successful!"})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "train_msg": f"❌ Error: {e}"})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
