from fastapi import APIRouter


router = APIRouter()


@router.get("/", summary="Hello World")
def hello():
    return {"Hello": "World"}
