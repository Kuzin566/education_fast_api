from fastapi import FastAPI

from app.routers import category, products

# app = FastAPI(swagger_ui_parameters={
#     "syntaxHighlight.theme": "obsidian",
#     "tryItOutEnabled": True,
#     "requestSnippetsEnabled	": False,
#     "queryConfigEnabled": False,
#     "persistAuthorization": False,
#     "request.curlOptions":False,
#     "showExtensions": False,
#     "showCommonExtensions": False,
#     "urls": 'Topbar'
# })


app = FastAPI()


@app.get("/", tags=['main'])
async def welcome() -> dict:
    return {
        "message": "My e-commerce app"
    }


app.include_router(category.router)
app.include_router(products.router)
