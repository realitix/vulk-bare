# Vulk-Bare

Vulk-Bare is a bare metal library for the Vulk 3D engine.
It provides a lot of tools.

[VULK 3D ENGINE](https://github.com/realitix/vulk)

## Provided functions

```python
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
```
