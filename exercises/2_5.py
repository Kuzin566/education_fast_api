from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/{username}")
async def login(username: Annotated[str, Path(min_length=3,
                                              max_length=15,
                                              description='Enter your username',
                                              example='Ilya')],
                age: int) -> dict:
    return {
        "user": username,
        "age": age
    }
