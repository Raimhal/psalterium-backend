from fastapi import FastAPI
from routes import router
from config import dependencies
from fastapi.middleware.cors import CORSMiddleware
from starlette.types import ASGIApp, Scope, Receive, Send



app = FastAPI()
# app = FastAPI(docs_url=None, redoc_url=None)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SimpleASGIMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        await self.app(scope, receive, send)
        client = scope["client"]
        print(f"[CLIENT]: {client}")


app.add_middleware(SimpleASGIMiddleware)

dependencies.create_database()
app.include_router(router)

