import uvicorn
from fastapi import FastAPI
from .routers import posts, users, login


app = FastAPI()
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(login.router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
