# main.py ထဲတွင်
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response
