from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/user/{username}")
async def login(
        user_name: Annotated[str, Path(min_length=3,
                                       max_length=15,
                                       description='Enter your username',
                                       example='permin0ff',
                                       alias='userName')],
        first_name: str | None = Query(max_length=10, ge=0, default=None, alias='firstName'),
        age: int = Query(ge=1, description='Enter your age', default=1),
        people: list[str] = Query(example='nick, pety'),
        value: str = Query(pattern='^J|s$', default=None)) -> dict:
    return {
        "user": user_name,
        "Name": first_name,
        "Age": age,
        "People": people,
        "Value": value
    }
