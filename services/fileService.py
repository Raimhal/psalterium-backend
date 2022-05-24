import os
from uuid import uuid4
from fastapi import UploadFile
from fastapi.responses import FileResponse
from PIL import Image, ImageFile


static_files_path = os.path.join(os.getcwd(), 'static\\files')
static_assets_path = os.path.join(os.getcwd(), 'static\\assets')


def save_file(file: UploadFile, height: int) -> str:
    print(file.__dict__)
    _, ext = file.filename.rsplit('.', 1)
    filename = f'{uuid4()}.{ext}'
    location = os.path.join(static_files_path, filename)
    img = Image.open(file.file)
    ratio = (height / float(img.size[1]))
    width = int((float(img.size[0]) * float(ratio)))
    img = img.resize((width, height), Image.ANTIALIAS)
    type = file.content_type.split('/')[1]
    img.save(location, type, quality=80, optimize=True, progressive=True)
    return filename

def get_file(path: str) -> FileResponse:
    full_path = get_full_path(static=static_files_path, path=path)
    if not os.path.exists(full_path):
        full_path = get_full_path(static=static_assets_path, path='default.png')
    return FileResponse(full_path)

def delete_file(path: str):
    full_path = get_full_path(static=static_files_path,path=path)
    if os.path.exists(full_path):
        os.remove(full_path)


def get_full_path(static: str, path: str):
    return os.path.join(static, path)
