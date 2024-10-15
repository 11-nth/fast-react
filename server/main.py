from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import get_db_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "https://flask-react-sqrc.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/api/users")
async def fetch_users():
    # Use async with to automatically manage the connection
    async with await get_db_connection() as conn:  # <-- add `await` here
        try:
            # Fetch data from the users table
            rows = await conn.fetch("SELECT user_id, user_name FROM users;")
            return [{"user_id": row["user_id"], "user_name": row["user_name"]} for row in rows]
        except Exception as e:
            print(f"Error executing query: {e}")
            return {"error": str(e)}


# if __name__ == '__main__':
#     import uvicorn, os
#     uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
