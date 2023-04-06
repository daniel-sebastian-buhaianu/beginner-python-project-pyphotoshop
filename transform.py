from image import Image
import numpy as np

def adjust_brightness(image, factor):
    # when we adjust the brightness, we just want to scale each value by some amount
    # factor is a value > 0, how much you want to brigthen the image by 
    # (< 1 = darken, > 1 = brigthen)
    x_pixels, y_pixels, num_channels = image.array.shape

    # make an empty image so we don't mutate the one we've got
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    # non-vectorized implementation
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_img.array[x, y, c] = image.array[x, y, c] * factor

    # vectorized version
    new_img.array = image.array * factor
    
    return new_img

def adjust_contrast(image, factor, mid=0.5):
    # adjust the contrast by increasing the difference
    # from the user-defined midpoint by some amount, factor
    x_pixels, y_pixels, num_channels = image.array.shape
    new_img = Image(x_pixels=x_pixels, y_pixels=y_pixels, num_channels=num_channels)

    # non-vectorized
    # for x in range(x_pixels):
    #     for y in range(y_pixels):
    #         for c in range(num_channels):
    #             new_img.array[x, y, c] = (image.array[x, y, c] - mid) * factor + mid

    # vectorized
    new_img.array = (image.array - mid) * factor + mid

    return new_img

if __name__ == "__main__":
    lake = Image(filename="lake.png")
    city = Image(filename="city.png")

    # # brighten
    # brightened_img = adjust_brightness(lake, 1.7)
    # brightened_img.write_image("brightened.png")

    # # darken
    # darkened_img = adjust_brightness(lake, 0.3)
    # darkened_img.write_image("darkened.jpg")

    # adjust the contract for the lake
    incr_contrast = adjust_contrast(lake, 2, 0.5)
    incr_contrast.write_image("incr_contrast.png")

    # decrease contrast
    decr_contrast = adjust_contrast(lake, 0.5, 0.5)
    decr_contrast.write_image("decr_contrast.png")