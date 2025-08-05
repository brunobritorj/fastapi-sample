from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from utils.msentra import msal_auth, secret_key
import routes 

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.include_router(msal_auth.router)
app.include_router(routes.me.router, prefix="/me", tags=["me"])


@app.get("/")
def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
