from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/users")
def get_users():
    return {
        'users': [
            'eze',
            'coi',
            'chukoy',
            'chooks',
            'ezekiel'
        ]
    }

# if __name__ == '__main__':
#     import uvicorn, os
#     uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

