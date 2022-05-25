import os
from uuid import uuid4
from fastapi import UploadFile
from fastapi.responses import FileResponse
import cloudinary
import cloudinary.uploader
import pathlib


def save_image(file: UploadFile, width: int, height: int) -> str:
    result = cloudinary.uploader.upload_large(
        file.file,
        public_id=f"images/{uuid4()}",
        resource_type="image",
        overwrite=True,
        eager = [
            {"width": width, "height": height, "crop": "thumb"}
        ],
        eager_async=True
    )
    return result.get("url")

def delete_file(path: str):
    path_to_image = "/".join(path.split("/")[-2:])
    cloudinary.uploader.destroy(path_to_image)
