import numpy as np

def convolutional(list,kernel):
    """Calculate the Activation given a Input list using a kernel

    Args:
        list: Input list
        kernel[list]: Kernel to calculate the activation

    Return:
        list: Activations

    """
    
    A = []

    # If kernel consists of 3 weights

    for j in range(2,len(list)-1,1):
        A.append(sum([list[j-1]*kernel[0],list[j]*kernel[1],list[j+1]*kernel[2]]))

    return A


# 1 lateral inhibition
w = 0.1
I = [1,1,1,1,1,0,0,0,0,0]
kernel = [-w,1,-w]
print(convolutional(I, kernel))

# 2 optical illusion
w = 0.1
I = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
kernel = [-w,1,-w]
print(convolutional(I, kernel))
