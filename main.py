import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import image
from routes import jwt

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins, you can use ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"]  # Allow all headers
)

app.include_router(image.router)
app.include_router(jwt.router)

@app.get("/")
def read_root():
    return {"Heartbeat": "I am still alive!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)