import cv2
import numpy as np
from Parameters import *


def countDots(path):
    # Read image in grayscale
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    # Apply blur
    image = cv2.blur(image, (2, 2))

    # Create Parameters instance
    params = Parameters()

    # Configure blob detector parameters
    detectorParams = cv2.SimpleBlobDetector_Params()
    detectorParams.filterByArea = params.filterByArea
    detectorParams.minArea = params.minArea
    detectorParams.filterByCircularity = params.filterByCircularity
    detectorParams.minCircularity = params.minCircularity
    detectorParams.filterByConvexity = params.filterByConvexity
    detectorParams.minConvexity = params.minConvexity
    detectorParams.filterByInertia = params.filterByInertia
    detectorParams.minInertiaRatio = params.minInertiaRatio

    # Create blob detector
    detector = cv2.SimpleBlobDetector_create(detectorParams)

    # Detect keypoints
    keypoints = detector.detect(image)

    # Create blank image for drawing keypoints
    blank = np.zeros((1, 1))
    
    # Draw keypoints on the original image
    blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Count the number of keypoints
    count = len(keypoints)

    if params.debug:
        cv2.imwrite(params.debugImg, blobs)

    return count
