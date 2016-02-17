""" 
@author: Leon Lam (@leonjunwei)
Last updated: 02/14/16 """

import random
from PIL import Image
import math



def build_random_function(min_depth, max_depth, xOrY): #if xOrY = 0, it takes X - otherwise it takes Y
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    startDepth = random.randint(min_depth,max_depth)
    buildingBlocks = {

    # 0:(lambda a,b: a * b),
    # 1:(lambda a,b: 0.5*(a+b)),
    # 2:(lambda a,b: math.cos(math.pi*a)),
    # 3:(lambda a,b: math.sin(math.pi*a)),
    # 4:(lambda a,b: a),
    # 5:(lambda a,b: b),

    # 6:(lambda a,b: (2.0 * a + b)/3.0),
    # 7:(lambda a,b: (a + 2.0 * b)/3.0)  
    }



    def generator(depth, xOrY):
        if depth == 1:
            if xOrY == 0:
            # n = random.randint(0,1)
            # if n == 0:
                return lambda x,y: x
            else:
                return lambda x,y: y
            # else:
            #     return lambda x,y: y
        else:
            n = random.randint(0,5)
            if n == 0:
                return lambda x,y: generator(depth-1, xOrY)(x,y)
            elif n == 1:
                return lambda x,y: generator(depth-1, xOrY)(x,y)
            elif n == 2:
                return lambda x,y: math.cos(math.pi*generator(depth-1, xOrY)(x,y))
            elif n == 3:
                return lambda x,y: math.sin(math.pi*generator(depth-1, xOrY)(x,y))
            elif n == 4:
                return lambda x,y: generator(depth-1, xOrY)(x,y)*generator(depth-1, xOrY)(x,y)
            elif n == 5:
                return lambda x,y: 0.5*(generator(depth-1, xOrY)(x,y) + generator(depth-1, xOrY)(x,y))

    return generator(startDepth, xOrY)

# print build_random_function(7,9)
# a = 1
# b = 2
# a = build_random_function(7,9)
# print a(1.3,2)

# print x(a,b)




# def evaluate_random_function(f, x, y):
#     """ Evaluate the random function f with inputs x,y
#         Representation of the function f is defined in the assignment writeup

#         f: the function to evaluate
#         x: the value of x to be used to evaluate the function
#         y: the value of y to be used to evaluate the function
#         returns: the function value

#         >>> evaluate_random_function(["x"],-0.5, 0.75)
#         -0.5
#         >>> evaluate_random_function(["y"],0.1,0.02)
#         0.02
#     """
#     if f == ["x"]:
#         return x
#     elif f == ["y"]:
#         return y


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    return float(val-input_interval_start)*(output_interval_end - output_interval_start)/(input_interval_end - input_interval_start)+output_interval_start


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


# def test_image(filename, x_size=350, y_size=350):
#     """ Generate test image with random pixels and save as an image file.

#         filename: string filename for image (should be .png)
#         x_size, y_size: optional args to set image dimensions (default: 350)
#     """
#     # Create image and loop over all pixels
#     im = Image.new("RGB", (x_size, y_size))
#     pixels = im.load()
#     for i in range(x_size):
#         for j in range(y_size):
#             x = remap_interval(i, 0, x_size, -1, 1)
#             y = remap_interval(j, 0, y_size, -1, 1)
#             pixels[i, j] = (random.randint(0, 255),  # Red channel
#                             random.randint(0, 255),  # Green channel
#                             random.randint(0, 255))  # Blue channel

#     im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(2, 3, 0)
    green_function = build_random_function(2, 3, 1)
    blue_function = build_random_function(2, 3, 0)
    a = red_function
    b = blue_function
    c = green_function
    # print a(1,2)
    # print b(1,2)
    # print c(1,2)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()           
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(a(x, y)),
                    color_map(b(x, y)),
                    color_map(c(x, y))
                    )

    im.save(filename)


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
generate_art("myart.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
# test_image("noise.png")
