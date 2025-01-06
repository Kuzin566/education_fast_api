from fastapi import FastAPI

app = FastAPI()

country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
}


@app.get('/country/{country}')
async def list_cities(country: str, limit: int) -> dict:
    return {
        'country': f'{country}',
        'cities': country_dict.get(country, [])[:limit]
    }


