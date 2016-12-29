from cffi import FFI
from os import path

HERE = path.dirname(path.realpath(__file__))

ffi = FFI()

ffi.cdef('''
    unsigned char*
    stbi_load_from_memory(unsigned char const *buffer, int len, int *x,
                          int *y, int *channels_in_file,
                          int desired_channels);
    ''')

ffi.set_source('_vulkbare',
               '#define STB_IMAGE_IMPLEMENTATION' +
               open(path.join(HERE, 'stb_image.h')).read())
