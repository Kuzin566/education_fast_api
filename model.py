from pydantic import BaseModel, Field


class Item(BaseModel):
    description: str | None = None
    text: str = "Simple text"


class Message(BaseModel):
    id: int
    description: str | None = Field(default=None,
                                    description="The description of the message",
                                    max_length=300)
    text: str = None
    item: Item


a = Message
a.id = 5
print(a.dict)
