'''Main functions exported by vulkbare.

User shouldn't use directly _vulkbare module but this one.
'''
from vulkbare._vulkbare import ffi, lib

__all__ = ['load_image']


def load_image(buf, request_components=0):
    '''Load a png or jpeg image into a bitmap buffer.

    *Parameters:*

    - `buf`: Buffer to load
    - `request_components`: If you want to force the number of components

    *Returns:*

    A tuple containing:

    - Bitmap buffer
    - width of bitmap
    - height of bitmap
    - number of components
    '''
    x = ffi.new('int*')
    y = ffi.new('int*')
    n = ffi.new('int*')

    cbuf = ffi.from_buffer(buf)

    bitmap = lib.stbi_load_from_memory(
        ffi.cast('unsigned char*', cbuf), len(buf), x, y, n,
        request_components)

    pybuffer = ffi.buffer(bitmap, x[0]*y[0]*n[0])

    return pybuffer, x[0], y[0], n[0]
