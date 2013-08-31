import os
from PIL import Image
from cv2 import (imread, TM_CCORR_NORMED, matchTemplate, rectangle, normalize,
                 NORM_MINMAX, minMaxLoc)

from formats import pil2numpy, numpy2pil
import numpy

DATA_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
SOURA_BEGINNING = imread(os.path.join(DATA_DIRECTORY, "SOURA_BEGINNING.jpg"))
AYAT_SEPARATOR = imread(os.path.join(DATA_DIRECTORY, "AYAT_SEPARATOR.png"))
LAYOUT = imread(os.path.join(DATA_DIRECTORY, "LAYOUT.jpg"))


def search_image(num_image, num_template, threshold=0.99):
    '''
    TODO: return list of tuples representing x,y positions of the quested
    object within the image
    '''
    result = matchTemplate(num_image, num_template, TM_CCORR_NORMED)
    loc = numpy.where(result >= threshold)

    return loc


def fillin_template(background, image, positions):
    '''
    Keyword arguments:
        background -- the template image to be filled in
        image -- the image that would be pasted on the background
        positions -- list of positions where image should be pasted
    Returns:
        the template image with pics from data pasted on it
    '''
    for position in zip(*positions[::-1]):
        background.paste(image, position)
    return background


def layout_handler((image, index, layout, page)):
    num_img = pil2numpy(image)

    layout_location = matchTemplate(num_img, LAYOUT, TM_CCORR_NORMED)
    min_x, max_y, minloc, maxloc = minMaxLoc(layout_location)

    layout.paste(numpy2pil(LAYOUT), maxloc)
    return image, index, layout, page


def ayat_handler((image, index, layout, page)):
    num_img = pil2numpy(image)
    ayat_location = search_image(num_img, AYAT_SEPARATOR, threshold=0.959)
    layout = fillin_template(layout, numpy2pil(AYAT_SEPARATOR), ayat_location)
    return image, index, layout, page


def soura_handler((image, index, layout, page)):
    num_img = pil2numpy(image)
    soura_location = search_image(num_img, SOURA_BEGINNING, threshold=0.935)
    layout = fillin_template(layout, numpy2pil(SOURA_BEGINNING), soura_location)
    return image, index, layout, page
