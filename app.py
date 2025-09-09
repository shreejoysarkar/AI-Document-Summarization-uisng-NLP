from fastapi import FastAPI, Request, Form, UploadFile, File
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
    return templates.TemplateResponse("index.html", {"request": request, "result": None, "input_text": ""})


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


@app.post("/predict_file", response_class=HTMLResponse)
async def predict_file(request: Request, file: UploadFile = File(...)):
    try:
        if file.filename.endswith(".pdf"):
            import PyPDF2
            reader = PyPDF2.PdfReader(file.file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
        elif file.filename.endswith(".docx"):
            import docx
            doc = docx.Document(file.file)
            text = "\n".join([para.text for para in doc.paragraphs])
        else:
            return templates.TemplateResponse("index.html", {"request": request, "result": "Unsupported file type."})

        obj = PredictionPipeline()
        summary = obj.predict(text)
        return templates.TemplateResponse("index.html", {"request": request, "result": summary, "input_text": text})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "result": f"Error: {e}"})

if __name__ == "__main__":
    uvicorn.run(app)
