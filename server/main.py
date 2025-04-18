import os
import cv2
import uuid
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="AI Studio API",
    description="Image to Video Conversion Service",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Create necessary directories
os.makedirs("temp", exist_ok=True)
os.makedirs("output", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.middleware("http")
async def log_requests(request, call_next):
    """Middleware to log all incoming requests"""
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response

def validate_file(file: UploadFile):
    """Validate uploaded file"""
    allowed_types = ["image/jpeg", "image/png", "image/webp"]
    max_size = 10 * 1024 * 1024  # 10MB
    
    if file.content_type not in allowed_types:
        raise HTTPException(400, "Only JPEG/PNG/WEBP images are allowed")
    
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)
    
    if file_size > max_size:
        raise HTTPException(400, "File too large (Max 10MB)")

async def process_image_to_video(
    file: UploadFile, 
    output_fps: int = 24, 
    duration: int = 3
) -> str:
    """Core processing function"""
    try:
        # Generate unique filename
        file_ext = file.filename.split(".")[-1]
        temp_filename = f"temp/{uuid.uuid4()}.{file_ext}"
        output_filename = f"output/{uuid.uuid4()}.mp4"
        
        # Save uploaded file
        with open(temp_filename, "wb") as buffer:
            buffer.write(await file.read())
        
        # Process with OpenCV
        img = cv2.imread(temp_filename)
        if img is None:
            raise ValueError("Invalid image file")
            
        height, width = img.shape[:2]
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(
            output_filename,
            fourcc,
            output_fps,
            (width, height)
        
        # Generate video frames
        for _ in range(output_fps * duration):
            video_writer.write(img)
        
        video_writer.release()
        
        # Cleanup temp file
        os.remove(temp_filename)
        
        return output_filename
        
    except Exception as e:
        logging.error(f"Processing error: {str(e)}")
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        raise HTTPException(500, f"Processing failed: {str(e)}")

@app.post("/convert")
async def convert_image(
    file: UploadFile = File(...),
    duration: Optional[int] = 3,
    fps: Optional[int] = 24
):
    """
    Convert image to video with:
    - file: Image file (JPEG/PNG)
    - duration: Video duration in seconds (default: 3)
    - fps: Frames per second (default: 24)
    """
    # Validate input
    validate_file(file)
    
    if duration <= 0 or duration > 10:
        raise HTTPException(400, "Duration must be between 1-10 seconds")
    
    if fps < 10 or fps > 60:
        raise HTTPException(400, "FPS must be between 10-60")
    
    # Process conversion
    try:
        output_path = await process_image_to_video(file, fps, duration)
        return {"status": "success", "video_url": f"/static/{os.path.basename(output_path)}"}
    
    except Exception as e:
        logging.error(f"Conversion error: {str(e)}")
        raise HTTPException(500, "Conversion failed")

@app.get("/static/{filename}")
async def serve_video(filename: str):
    """Serve converted videos"""
    video_path = f"output/{filename}"
    if not os.path.exists(video_path):
        raise HTTPException(404, "File not found")
    return FileResponse(video_path)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# server/main.py
from fastapi import FastAPI, Depends
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
import redis.asyncio as redis

app = FastAPI(
    title="AI Studio",
    dependencies=[Depends(RateLimiter(times=100, minutes=1))]
)

@app.on_event("startup")
async def startup():
    redis_connection = redis.from_url("redis://localhost:6379")
    await FastAPILimiter.init(redis_connection)
