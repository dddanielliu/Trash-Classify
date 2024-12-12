from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from ClassifyInterface import ClassifyInterface
import asyncio
import os
import sys

app = FastAPI()

ClassifyIntf = None

@app.on_event("startup")
async def load_data():
    global ClassifyIntf
    ClassifyIntf = ClassifyInterface()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict/")
async def predict(img_path: str = ""):
    img_path = os.path.abspath(img_path)
    
    # Check if the file exists
    if not os.path.isfile(img_path):
        raise HTTPException(status_code=404, detail="Image file not found")
    
    print(img_path)
    result = ClassifyIntf.predict(img_path)
    # return result
    return JSONResponse(content=result, media_type="application/json; charset=utf-8")
