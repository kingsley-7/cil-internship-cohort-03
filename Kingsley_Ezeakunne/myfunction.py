import os
from typing import Union
from PIL import Image


def resize_image(input_path: Union[str, os.PathLike], output_path: Union[str, os.PathLike], size: tuple[int]):
    im = Image.open(input_path)
    im_resize = im.resize(size)
    im_resize.save(output_path)


resize_image('Nature.jpg', 'Nature-resize.jpg', (100, 100))
