from functools import lru_cache


class ImagesService:
    async def get_images(self):
        return 'Hello images!'


@lru_cache
def get_images_service() -> ImagesService:
    return ImagesService()
