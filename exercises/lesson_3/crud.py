from typing import Annotated

from fastapi import Body, FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Message(BaseModel):
    id: int | None = None
    text: str

    model_config = {
        "json_schema_extra": {
            "examples":
                [
                    {
                        "text": "Simple message",
                    }
                ]
        }
    }


messages_db: list[Message] = []


@app.get(path="/")
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request,
                                      "message.html",
                                      {
                                          "messages": messages_db
                                      })


@app.get(path="/message/{message_id}")
async def get_message(message_id: int) -> Message:
    try:
        return messages_db[message_id]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@app.post(path="/message", status_code=status.HTTP_201_CREATED)
async def create_message(message: Message) -> str:
    if messages_db:
        message.id = max(messages_db, key=lambda m: m.id).id + 1
    else:
        message.id = 0
    messages_db.append(message)
    return f"Message created! ID: {message.id}"


@app.put(path="/message/{message_id}")
async def update_message(message_id: int, message: Annotated[str, Body()]) -> str:
    try:
        edit_message = messages_db[message_id]
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    edit_message.text = message
    return "Message updated!"


@app.delete(path="/message/{message_id}")
async def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f"Message ID={message_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")


@app.delete(path="/")
async def kill_message_all() -> str:
    messages_db.clear()
    return "All messages deleted!"
