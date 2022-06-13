import colorgram


def extract_colors(num_of_colors):
    rgbcolors = []
    colors = colorgram.extract('image.jpeg', num_of_colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_tuple = (r, g, b)
        rgbcolors.append(rgb_tuple)

    return rgbcolors
