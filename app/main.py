from fastapi import FastAPI, File, UploadFile
from app.analyzer import analyze_audio
import tempfile
import os

app = FastAPI()

@app.post("/analyze/")
async def analyze_audio_endpoint(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=file.filename[-4:]) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    bpm, note, mode = analyze_audio(tmp_path)
    os.remove(tmp_path)

    return {
        "filename": file.filename,
        "bpm": bpm,
        "key": f"{note} {mode}"
    }
