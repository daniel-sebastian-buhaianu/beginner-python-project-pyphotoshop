from image import Image
import numpy as np

def adjust_brightness(image, factor):
    # when we adjust the brightness, we just want
    # to scale each value by some amount
    # factor is a value > 0, how much you want to brigthen
    # the image by (< 1 = darken, > 1 = brigthen)
    x_pixels, y_pixels, num_channels = image.array.shape

    # make an empty image so we don't mutate
    # the one we've got
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_img.array[x, y, c] = image.array[x, y, c] * factor
    
    return new_img


if __name__ == "__main__":
    lake = Image(filename="lake.png")
    city = Image(filename="city.png")

    # let's lighten the lake
    brightened_img = adjust_brightness(lake, 1.7)
    brightened_img.write_image("brightened.png")