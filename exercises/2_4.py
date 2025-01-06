from fastapi import FastAPI

app = FastAPI()


# @app.get('/product/{idx}')
# async def detail_view(idx: int) -> dict:
#     return {
#         'product': f'Stock number {idx}'
#     }
#
#
# @app.get('/users/{name}/{age}')
# async def users(name: str, age: int) -> dict:
#     return {
#         'user_name': f'{name}',
#         'user_age': age
#     }


@app.get('/users/admin')
async def admin() -> dict:
    return {
        'message': 'Hello admin'
    }


@app.get('/users/{name}')
async def users(name: str) -> dict:
    return {
        'user_name': f'{name}',
    }


@app.get('/product')
async def detail_view(item_id: int) -> dict:
    return {
        'product': f'Stock number {item_id}'
    }


@app.get('/users')
async def users(name: str = 'Undefined', age: int = 18) -> dict:
    return {
        'user_name': f'{name}',
        'user_age': age
    }
