from cv2 import circle
from Parameters import *

import cv2
import numpy as np


def countDots(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = cv2.blur(image,(2,2))

    params = Parameters()
    detectorParams = cv2.SimpleBlobDetector_Params()

    detectorParams.filterByArea = params.filterByArea
    detectorParams.minArea = params.minArea

    detectorParams.filterByCircularity = params.filterByCircularity
    detectorParams.minCircularity = params.minCircularity

    detectorParams.filterByConvexity = params.filterByConvexity
    detectorParams.minConvexity = params.minConvexity
        
    detectorParams.filterByInertia = params.filterByInertia
    detectorParams.minInertiaRatio = params.minInertiaRatio

    detector = cv2.SimpleBlobDetector_create(detectorParams)

    keypoints = detector.detect(image)

    blank = np.zeros((1, 1))
    blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),
                            cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    count = len(keypoints)

    if params.debug:
        cv2.imwrite(params.debugImg, blobs) 

    return count
