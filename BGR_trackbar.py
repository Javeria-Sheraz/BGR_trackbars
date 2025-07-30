import cv2 as cv
import numpy as np

# While creating track bars we need a function. Because when a slider is moved some function is to be executed.
# However, in this case we don't need to call any function when the slider is moved so we make an empty function and pass it in create track bar setup
# This function reads the current track bar position as X but we choose to ignore it because in loop we read the position of track bar using separate methods for three channels
def nothing(x):
    pass

#Using numpy recreated a window of pixels. Syntax is (height, width, channels)
img = np.zeros((580,950,3), np.uint8)

cv.namedWindow('image')
# First three create sliders for each color while the 4th one creates a slider for switch
cv.createTrackbar('Blue', 'image', 0, 255, nothing)
cv.createTrackbar('Green', 'image', 0, 255, nothing)
cv.createTrackbar('Red', 'image', 0, 255, nothing)
cv.createTrackbar('OFF || ON', 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)

    # Press escape key to close the window
    k = cv.waitKey(1)
    if k == 27:
        break

    B = cv.getTrackbarPos('Blue', 'image')
    G = cv.getTrackbarPos('Green', 'image')
    R = cv.getTrackbarPos('Red', 'image')
    Sw = cv.getTrackbarPos('OFF || ON', 'image')

    # If the switch is closed all the three channels of image are replaced by black color
    if Sw ==0:
        img[:] = 10
        cv.putText(img, "Switch ON to see the colour", (80, 290), cv.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 5)
        cv.putText(img, "Switch ON to see the colour", (80, 290), cv.FONT_HERSHEY_COMPLEX, 1.5, (0, 0, 0), 3)
    else:
        img[:] = [B, G, R]
    #if the switch is open the image window is filled with the colors selected from the sliders

cv.destroyAllWindows()
