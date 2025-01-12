from fastapi import Depends, FastAPI, Query
from starlette.requests import HTTPException, Request

log_user = []


def log_client(request: Request):
    log_user.append(request.headers)


app = FastAPI(dependencies=[Depends(log_client)])


class Paginator:
    def __init__(self):
        self.limit = 10
        self.page = 1

    def __call__(self, limit: int):
        if limit < self.limit:
            return [{
                'limit': self.limit,
                'page': self.page
            }]
        else:
            return [{
                'limit': limit,
                'page': self.page
            }]


async def sub_dependency(request: Request) -> str:
    return request.method


async def main_dependency(sub_dependency_value: str = Depends(sub_dependency)) -> str:
    return sub_dependency_value


@app.get("/log_user")
async def print_log_user():
    return {
        "user": log_user
    }


@app.get("/test/")
async def test_endpoint(test: str = Depends(main_dependency)):
    return test


async def pagination_path_func(page: int):
    if page < 0:
        raise HTTPException(status_code=404, detail="Page does not exist")
    if page == 0:
        raise HTTPException(status_code=400, detail="Invalid page value")


async def pagination_func(limit: int = Query(default=10, qe=0), page: int = 1):
    return [{
        'limit': limit,
        'page': page
    }]


my_paginator = Paginator()


@app.get("/messages", dependencies=[Depends(pagination_path_func)])
async def all_message(pagination: dict = Depends(pagination_func)):
    return {
        "messages": pagination
    }


@app.get("/comments")
async def all_comments(pagination: list = Depends(pagination_func)):
    return {
        "comments": pagination
    }
