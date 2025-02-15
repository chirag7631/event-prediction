from fastapi import FastAPI
from api.predict import router as predict_router

# Initialize FastAPI app
app = FastAPI()

# Include the prediction router
app.include_router(predict_router)

@app.get('/health')
async def health():
    """
    Returns health status
    """
    return {'status': 'ok'}
