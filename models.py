from typing import List

from pydantic import BaseModel, Field


class VideoData(BaseModel):
    vidId: str
    title: str
    url: str
    cover: str


class BasicResponseModel(BaseModel):
    code: int = Field(200, example=200)
    message: str = Field("success", example="success")


class VideoResponseModel(BasicResponseModel):
    data: List[VideoData] = Field([])
