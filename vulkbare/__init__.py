'''Main functions exported by vulkbare.

User shouldn't use directly _vulkbare module but this one.
'''
from vulkbare._vulkbare import ffi, lib

__all__ = ['load_image']


class ResizeError(Exception):
    pass


def load_image(buf, request_components=0):
    """Load a png or jpeg image into a bitmap buffer.

    Args:
        buf (Buffer): Buffer to load
        request_components (int): If you want to force number of components

    Returns:

        A tuple containing:

        - Bitmap buffer
        - width of bitmap
        - height of bitmap
        - number of components
    """
    x = ffi.new('int*')
    y = ffi.new('int*')
    n = ffi.new('int*')

    cbuf = ffi.from_buffer(buf)

    bitmap = lib.stbi_load_from_memory(
        ffi.cast('unsigned char*', cbuf), len(buf), x, y, n,
        request_components
    )

    pybuffer = ffi.buffer(bitmap, x[0]*y[0]*n[0])

    return pybuffer, x[0], y[0], n[0]


def resize_image(buf, width, height, num_channels, new_width, new_height):
    """Resize an image

    Args:
        buf (Buffer): Buffer coming from `load_image`
        width (int): Width of `buf`
        height (int): Height of `buf`
        num_channels (int): Number of channels in `buf` (RGBA=4)
        new_width (int): Desired width
        new_height (int): Desired height

    Returns:
        Buffer: Resized image

    Raises:
        ResizeError: If an error occurs during resize
    """
    new_size = new_width * new_height * num_channels
    input_pixels = ffi.from_buffer(buf)
    output_pixels = ffi.new('unsigned char[]', new_size)

    result = lib.stbir_resize_uint8(
        ffi.cast('unsigned char*', input_pixels), width, height, 0,
        output_pixels, new_width, new_height, 0, num_channels
    )

    if not result:
        raise ResizeError()

    return ffi.buffer(output_pixels, new_size)
