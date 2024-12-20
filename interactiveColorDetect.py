import cv2
import glob
import numpy as np

# Mouse callback function
def showPixelValue(event, x, y, flags, param):
    global img, combinedResult, placeholder

    if event == cv2.EVENT_MOUSEMOVE and img is not None:
        # Get the value of pixel from the location of mouse in (x, y)
        bgr = img[y, x]

        # Convert the BGR pixel into other color formats
        ycb = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2YCrCb)[0][0]
        lab = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2Lab)[0][0]
        hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]

        # Create an empty placeholder for displaying the values
        placeholder = np.zeros((img.shape[0], 400, 3), dtype=np.uint8)

        # Fill the placeholder with the values of color spaces
        cv2.putText(placeholder, "BGR {}".format(bgr), (20, 70), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(placeholder, "HSV {}".format(hsv), (20, 140), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(placeholder, "YCrCb {}".format(ycb), (20, 210), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(placeholder, "LAB {}".format(lab), (20, 280), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 1, cv2.LINE_AA)

        # Combine the two results to show side by side in a single image
        combinedResult = np.hstack([img, placeholder])

        cv2.imshow('PRESS P for Previous, N for Next Image', combinedResult)


if __name__ == '__main__':
    # Load the images and setup the mouse callback function
    global img
    files = glob.glob('python/images/sample*.jpg')
    
    files.sort()

    if not files:
        print("No images found in the directory.")
        exit()

    i = 0
    img = cv2.imread(files[i])

    if img is None:
        print(f"Failed to load the image: {files[i]}")
        exit()

    img = cv2.resize(img, (400, 800))
    cv2.imshow('PRESS P for Previous, N for Next Image', img)

    # Create an empty window
    cv2.namedWindow('PRESS P for Previous, N for Next Image')
    # Create a callback function for any event on the mouse
    cv2.setMouseCallback('PRESS P for Previous, N for Next Image', showPixelValue)

    while True:
        k = cv2.waitKey(1) & 0xFF
        # Check next image in the folder
        if k == ord('n'):
            i += 1
            img = cv2.imread(files[i % len(files)])
            if img is None:
                print(f"Failed to load the image: {files[i % len(files)]}")
                continue
            img = cv2.resize(img, (400, 400))
            cv2.imshow('PRESS P for Previous, N for Next Image', img)

        # Check previous image in folder
        elif k == ord('p'):
            i -= 1
            img = cv2.imread(files[i % len(files)])
            if img is None:
                print(f"Failed to load the image: {files[i % len(files)]}")
                continue
            img = cv2.resize(img, (400, 400))
            cv2.imshow('PRESS P for Previous, N for Next Image', img)

        elif k == 27:  # Escape key
            cv2.destroyAllWindows()
            break

