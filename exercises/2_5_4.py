from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/user/{name}")
async def user(
        name: str = Path(min_length=4, max_length=20, description='Enter your name')) -> dict:
    return {
        'user_name': name,
    }


@app.get('/category/{category_id}/products')
async def category(category_id: Annotated[int, Path(gt=0, description='Category ID')],
                   page: Annotated[int, Query()] = None) -> dict:
    return {
        'category_id': category_id,
        'page': page
    }


profiles_dict = {
    'alex': {
        'name': 'Александр',
        'age': 33,
        'phone': '+79463456789',
        'email': 'alex@my-site.com'
    },
}


@app.get(f'/users')
async def retrieve_user_profile(username: Annotated[str, Query(min_length=2, max_length=50,
                                                               description='Имя пользователя'
                                                               )]) -> dict:
    return profiles_dict.get(username,
                             {
                                 'message': f'Пользователь {username} не найден.'
                             })
