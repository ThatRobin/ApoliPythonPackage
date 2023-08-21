from typing import List

import PIL
from PIL import Image

from datapack import Resourcepack


def process_image(infile, resourcepack: Resourcepack):
    im = Image.open(infile)

    i = 0

    try:
        while 1:
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            resourcepack.add_texture(new_im, f"animation/badapple/frame_{i}")
            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass # end of sequence