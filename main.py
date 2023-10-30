import json
import random

from fastapi import FastAPI, logger
from models import VideoData, VideoResponseModel, BasicResponseModel

VIDEO_DATABASE = []
DATABASE_FILE = "video_data.json"
VIDEO_AMOUNT = 5


def loadVideos():
    data = json.load(open(DATABASE_FILE, "r", encoding="utf-8"))
    for video in data:
        VIDEO_DATABASE.append(VideoData(**video))

    logger.logger.info("Loaded %d videos" % len(VIDEO_DATABASE))


loadVideos()
app = FastAPI()


@app.get("/videos",
         response_model=VideoResponseModel,
         description="Get a list of videos")
async def getVideos():
    try:
        resp = VideoResponseModel()
        resp.data = random.choices(VIDEO_DATABASE, k=VIDEO_AMOUNT)

        return resp
    except Exception as e:
        resp = BasicResponseModel(
            code=500,
            message=str(e)
        )
        return resp


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
