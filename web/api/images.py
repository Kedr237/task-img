from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from services.images import ImagesService, get_images_service

router = APIRouter()


@router.get('/')
async def get_images(
    images_service: ImagesService = Depends(get_images_service)
) -> str:
    images = await images_service.get_images()
    if not images:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

    return images
