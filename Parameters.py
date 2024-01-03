class Parameters:
    debug = True
    debugImg = '/tmp/debug.png'
    tmpImg = '/tmp/img.png'

    filterByArea, filterByColor, filterByInertia, filterByConvexity, filterByCircularity = True, False, True, True, True

    minArea, minCircularity, minConvexity, minInertiaRatio = 50, 0.6, 0.9, 0.7
