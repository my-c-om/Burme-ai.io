# server/main.py
from fastapi import FastAPI, UploadFile
import cv2
import numpy as np

app = FastAPI()

@app.post("/convert")
async def convert_image(file: UploadFile):
    # 1. Save uploaded image
    with open(f"temp/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())
    
    # 2. Simple OpenCV processing (Replace with real AI later)
    img = cv2.imread(f"temp/{file.filename}")
    height, width = img.shape[:2]
    
    # 3. Create sample video
    video_path = f"output/{file.filename}.mp4"
    writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'mp4v'), 24, (width, height))
    
    for _ in range(24 * 3):  # 3-second video
        writer.write(img)
    
    writer.release()
    return {"video_url": video_path}
