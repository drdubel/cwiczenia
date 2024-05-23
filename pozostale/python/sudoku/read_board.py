import glob
from pprint import pprint as print

import cv2
import numpy as np
import pytesseract


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def make_opening(image):
    kernel = np.ones((7, 7), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def make_canny(image):
    return cv2.Canny(image, 100, 200)


def main():
    paths = [*glob.glob("images/*.png")]
    print(paths)

    for path in paths:
        image = cv2.imread(path)

        cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
        cv2.imshow("Original", image)

        gray = get_grayscale(image)

        blurred = cv2.GaussianBlur(gray, (3, 3), 3)
        edged = cv2.Canny(blurred, 10, 100)

        cv2.namedWindow("Original2", cv2.WINDOW_NORMAL)
        cv2.imshow("Original2", edged)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        dilate = cv2.dilate(edged, kernel, iterations=1)
        contours, _ = cv2.findContours(
            dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        image_copy = image.copy()
        contours_img = image.copy()

        for i in range(len(contours)):
            cv2.drawContours(contours_img, contours, i, (0, 255, 0), 3)
            hull = cv2.convexHull(contours[i])
            epsilon = 0.15 * cv2.arcLength(hull, True)
            approx = cv2.approxPolyDP(hull, epsilon, True)

            if len(approx) == 4:
                distances = [
                    cv2.norm(approx[i] - approx[j])
                    for i in range(4)
                    for j in range(i + 1, 4)
                ]

                avg_distance = sum(distances) / len(distances)

                tolerance_percent = 50
                tolerance = avg_distance * tolerance_percent / 100

                equal_distances = all(
                    abs(distance - avg_distance) < tolerance for distance in distances
                )

                if equal_distances:
                    contour_area = cv2.contourArea(approx)
                    if contour_area > 100:
                        corners = approx.reshape(-1, 2)

                        rhombus_corners = np.float32(corners)

                        start = 5
                        new_corners = np.array(
                            [
                                [-start, -start],
                                [image_copy.shape[1] + start, -start],
                                [
                                    image_copy.shape[1] + start,
                                    image_copy.shape[0],
                                ],
                                [-start, image_copy.shape[0]],
                            ],
                            dtype=np.float32,
                        )

                        matrix = cv2.getPerspectiveTransform(
                            rhombus_corners, new_corners
                        )
                        warped_image = cv2.warpPerspective(
                            image_copy,
                            matrix,
                            (image_copy.shape[1], image_copy.shape[0]),
                            flags=cv2.INTER_LINEAR,
                        )

                        resized_image = cv2.resize(
                            warped_image, (warped_image.shape[1], warped_image.shape[1])
                        )

                        rotated_image = cv2.rotate(
                            resized_image, cv2.ROTATE_90_CLOCKWISE
                        )

                        cv2.namedWindow("Board", cv2.WINDOW_NORMAL)
                        cv2.imshow("Board", rotated_image)

                        cv2.waitKey(0)
                        cv2.destroyAllWindows()

                        board = np.zeros((3, 3, 3, 3), dtype=int)

                        for j in range(9):
                            for k in range(9):
                                width = rotated_image.shape[0] // 9
                                height = rotated_image.shape[1] // 9
                                x1 = j * width + start
                                y1 = k * height + start
                                x2 = (j + 1) * width - start
                                y2 = (k + 1) * height - start

                                tile = rotated_image[y1:y2, x1:x2]

                                custom_config = rf"--oem 3 --psm 6 -c tessedit_char_whitelist=123456789"

                                try:
                                    text = int(
                                        pytesseract.image_to_string(
                                            tile,
                                            config=custom_config,
                                        )
                                    )

                                except ValueError:
                                    text = 0

                                board[k // 3, j // 3, k % 3, j % 3] = text

                                print(text)

                                # cv2.namedWindow("Tile", cv2.WINDOW_NORMAL)
                                # cv2.imshow("Tile", tile)
                                # cv2.waitKey(0)
                                # cv2.destroyAllWindows()

                        print(board)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
