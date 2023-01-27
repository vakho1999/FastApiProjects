import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from app.src.controllers import TransactionController, DataTableParameterController

app = FastAPI()
origins = ["*","localhost"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(TransactionController.router)
app.include_router(DataTableParameterController.router)
add_pagination(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':

    uvicorn.run("main:app",  reload=True, host="0.0.0.0", port=9999)