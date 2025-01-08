from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {
        'message': 'My first project in FastAPI'
    }


@app.get('/hello/{user}')
async def welcome_user(user: str) -> dict:
    return {
        "user": f'Hello {user}'
    }


@app.get('/order/{order_id}', status_code=201, description='ручка ради поеботы',
         summary='order_id')
async def order(order_id: int) -> dict:
    return {
        "id": order_id
    }


@app.get("/user")
async def login(username: str, age: int = None) -> dict:
    return {
        "user": username,
        "age": age
    }


@app.get("/user/profile")
async def profile() -> dict:
    return {
        "profile": "View profile user"
    }


@app.get("/user/{user_name}")
async def user(user_name: str) -> dict:
    return {
        "user": user_name
    }


@app.get("/employee/{name}/company/{company}")
async def get_employee(name: str, department: str, company: str) -> dict:
    return {
        "Employee": name,
        "Company": company,
        "Department": department
    }
