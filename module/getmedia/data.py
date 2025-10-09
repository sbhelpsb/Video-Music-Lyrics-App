import pydantic

class MediaData(pydantic.BaseModel):
    title: str
    id: str
    audio_file_url: str
    lyrics_file_url: str | None = None