# Vulk-Bare

Vulk-Bare is a bare metal library for the Vulk 3D engine.
It provides a lot of tools.

[VULK 3D ENGINE](https://github.com/realitix/vulk)

## Provided functions

### load_image

```
(memoryview, x, y, n) = load_image(buffer, components=0)

Load an image in buffer (opened in binary mode) and return the corresponding
bitmap.

*Parameters:*

- `buffer`: A python buffer: open('file.png', 'rb').read()
- `components`: Number of desired components in image
                (R=1, RG=2, RGB=3, RGBA=4). If 0, it takes the image number.

*Returns:*

Tuple containing:

- `memoryview`: The bitmap in memoryview
- `x`: Image's width
- `y`: Image's height
- `n`: Number of channel in image (1, 2, 3, 4)
```
