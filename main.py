from fastapi import FastAPI

import credential_handler
import drive

app = FastAPI()

credential_handler.get_creds()

@app.get("/search")
async def search(file_name: str):
    return drive.search_file('test.json')


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
