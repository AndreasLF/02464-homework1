import cv2, sys
import numpy as np
# from skimage import io

np.set_printoptions(threshold=sys.maxsize)

def convolve2D(image, kernel, padding=0, strides=1):
    # Cross Correlation
    # kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        imagePadded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        imagePadded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(imagePadded)
    else:
        imagePadded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * imagePadded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output


def threshold(A, threshold):
    x = np.where(A < threshold, 0, 255)

    return x


# threshold(np.array([[1,2,3],[0.1,0.5,1],[1,2,1]]),0.6)

img_path = "MonaLisa.jpg"

# load the image
image = cv2.imread(img_path) 
image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

w = 0.1
base_kernel = np.array([[-w,-w,-w],[-w,1,-w],[-w,-w,-w]])

kernel2 = np.array([[-w,-w,-w,-w,-w,-w],[-w,-w,-w,-w,-w,-w],[-w,-w,1,1,-w,-w],[-w,-w,1,1,-w,-w],[-w,-w,-w,-w,-w,-w],[-w,-w,-w,-w,-w,-w]])

output = convolve2D(image, kernel2)
# print(output)

thres = 15

output = threshold(output,thres)
# print(output)

cv2.imwrite(f'data/2DConvolved_kernel2_threshold{thres}.jpg', output)
