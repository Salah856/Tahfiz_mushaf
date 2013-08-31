from PIL import Image
from cv2 import cv
import numpy


def pil2cv(pil_im):
    cv_im = cv.CreateImageHeader(pil_im.size, cv.IPL_DEPTH_8U, 3)
    cv.SetData(cv_im, pil_im.tostring())
    return cv_im


def pil2numpy(pil_im):
    num_im = numpy.array(pil_im)
    return num_im


def cv2pil(cv_im):
    pil_im = Image.fromstring("L", cv.GetSize(cv_im), cv_im.tostring())
    return pil_im


def cv2numpy(cv_im):
    num_im = numpy.array(cv2pil(cv_im))
    return num_im


def numpy2cv(num_im):
    cv_im = cv.fromarray(num_im)
    return cv_im


def numpy2pil(num_im):
    pil_im = Image.fromarray(num_im)
    return pil_im
