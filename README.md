
POST /convert
Content-Type: multipart/form-data

Params:
- file: Image (JPEG/PNG)  
- duration: Video length (3-10 sec)  
- style: Art style (van_gogh/ukiyoe)  
🖥️ UI Components
html
<!-- Main Structure -->
<div class="glass-panel">
  <canvas id="preview-canvas"></canvas>
  <input type="file" id="image-upload">
  <button id="convert-btn" class="pulse">
    <i class="fas fa-magic"></i> Convert
  </button>
</div>
🛠️ Configuration
python
# server/config.py
class Settings:
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_TYPES = ["image/jpeg", "image/png"]
    OUTPUT_FPS = 24
🐳 Docker Deployment
dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY server/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
📊 Project Structure
├── src/               # Frontend
│   ├── css/           # Glassmorphism styles
│   ├── js/            # Three.js components
│   └── index.html     # Main entry point
└── server/            # Backend
    ├── main.py        # FastAPI routes
    ├── ai_processor/  # CV algorithms
    └── tests/         # Pytest cases
📝 Notes
diff
+ New Features  
- Image preview before conversion  
- Style transfer options  
! Known Issues  
- Large files (>5MB) may timeout
Access at: http://localhost:8000
API Docs: http://localhost:8000/docs
Production Tip: Use Gunicorn with 4 workers for better performance
