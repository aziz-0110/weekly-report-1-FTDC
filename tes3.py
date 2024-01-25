import cv2
import numpy as np
import glob

# Dimensi papan catur
CHECKERBOARD = (6, 9)

# Membuat vektor untuk menyimpan 3D points dari setiap sudut papan catur
objpoints = []

# Membuat vektor untuk menyimpan 2D points (sudut) dari setiap sudut papan catur
imgpoints = []

# Membuat grid 3D untuk papan catur
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

# Extracting path of individual image stored in a given directory
images = glob.glob('./images1/*.jpg')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    if ret:
        objpoints.append(objp)

        # Zhang's method for corner subpixel accuracy
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)

print("Number of images with detected corners:", len(objpoints))

cv2.destroyAllWindows()


# Camera Calibration using Zhang's method
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Camera matrix:\n", mtx)
print("\nDistortion coefficients:\n", dist)

# Save the camera calibration results
np.savez('./calibration_results_zhang.npz', mtx=mtx, dist=dist)
