import asyncpg

# Database connection URL
DATABASE_URL = "postgresql://eleventh:1iHmDeTzgmiQZ86qCk80ApcKxnBbeAmG@dpg-cs73jt8gph6c73fd60pg-a.singapore-postgres.render.com/fast_react"

class DatabaseConnection:
    def __init__(self):
        self.conn = None

    # Implementing the async context manager entry method
    async def __aenter__(self):
        # Replace with your actual connection details
        self.conn = await asyncpg.connect(DATABASE_URL)
        return self.conn

    # Implementing the async context manager exit method
    async def __aexit__(self, exc_type, exc, tb):
        if self.conn:
            await self.conn.close()

# This function returns an instance of the DatabaseConnection class
async def get_db_connection():
    return DatabaseConnection()
