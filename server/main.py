# server/main.py ကို ဒီလိုမွမ်းမံပါ
from fastapi import BackgroundTasks
from PIL import Image
import numpy as np

async def process_video_in_background(image_path: str):
    # AI Model ကို တကယ်ချိတ်ဆက်ခြင်း
    img = Image.open(image_path)
    frames = []
    
    for i in range(24*5):  # 5-second video
        processed_frame = apply_ai_effects(img, frame_index=i)
        frames.append(processed_frame)
    
    save_as_mp4(frames, "output/result.mp4")

@app.post("/convert")
async def convert_image(file: UploadFile, background_tasks: BackgroundTasks):
    temp_path = f"temp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())
    
    background_tasks.add_task(process_video_in_background, temp_path)
    return {"message": "Processing started", "status_url": "/status/123"}
