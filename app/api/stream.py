from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time

router = APIRouter(prefix="/stream", tags=["stream"])


def generate():
    print("Generator started")

    yield "Hello\n"

    time.sleep(2)

    yield "Ayush\n"

    time.sleep(2)

    yield "How are you?\n"


@router.get("/")
def stream():
    return StreamingResponse(
        generate(),
        media_type="text/plain",
    )
