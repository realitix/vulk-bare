from cffi import FFI
from os import path

HERE = path.dirname(path.realpath(__file__))

ffi = FFI()

ffi.cdef('''
    unsigned char*
    stbi_load_from_memory(unsigned char const *buffer, int len, int *x,
                          int *y, int *channels_in_file,
                          int desired_channels);

    int
    stbir_resize_uint8(const unsigned char *input_pixels, int input_w,
                       int input_h , int input_stride_in_bytes,
                       unsigned char *output_pixels, int output_w,
                       int output_h, int output_stride_in_bytes,
                       int num_channels);
    ''')

ffi.set_source('_vulkbare',
               '#define STB_IMAGE_IMPLEMENTATION\n' +
               '#define STB_IMAGE_RESIZE_IMPLEMENTATION\n' +
               open(path.join(HERE, 'stb_image.h')).read() +
               open(path.join(HERE, 'stb_image_resize.h')).read()
               )
