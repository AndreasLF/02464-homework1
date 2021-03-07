import cv2, sys
import numpy as np

def create_kernel(n, w):
    """Generate kernel

    Args:
        n (int): kernel scale
        w (float): inhibiton weight

    Returns:
        ndarray: 2x2 kernel matrix
    """
    ones = np.ones((n,n))
    kernel = np.pad(ones,n,'constant', constant_values=-w)

    return kernel

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
    """Apply theshold to matrix

    Args:
        A (ndarray): matrix containing acrtivation levels
        threshold (int): threshold value

    Returns:
        ndarray: matrix with the threshold applied
    """
    x = np.where(A < threshold, 0, 255)

    return x

img_path = "hermann.jpg"

# load the image
image = cv2.imread(img_path) 
image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)


for n in range(1,21):
    w = 0.1
    # Threshold value. If None a threshold will not be applied
    thres = None

    # Generate the kernel
    kernel = create_kernel(n,w)

    # Apply the kernel to the image
    output = convolve2D(image, kernel)


    if thres: 
        # Apply threshold
        output = threshold(output,thres)
        cv2.imwrite(f'test_data/hermann_grid/2DConvolved_kernel{n}_threshold{thres}.jpg', output)
    else:
        cv2.imwrite(f'test_data/hermann_grid/2DConvolved_kernel{n}.jpg', output)