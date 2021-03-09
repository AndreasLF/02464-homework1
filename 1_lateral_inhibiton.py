import matplotlib.pyplot as plt

def activation_level(I,w):
    """ Calculate activation levels. 
    
    The activation of the two cells at the endpoints are ignored.

    Args:
        I (list[int]): Inputs from photoreceptor
        w (int): Weight of lateral inhibition

    Returns:
        List[float]: Activiation levels of each element
    """
    
    A = []
    
    for index, _ in enumerate(I):
        # If it is not the first and not the last element in the list
        if index != 0 and index != len(I)-1:
            # Calculate the activation level
            a = I[index] - w*(I[index-1]+I[index+1])
            A.append(a)
    return A

def set_threshold(A, threshold):
    """Activate or deactivate the nerons based on a threshold.

    Args:
        A (list[float]): List of activation levels
        threshold (float): The threshold value. If the activation level of a neron is smaller than this, it will not be active.

    Returns:
        list[int]: Active and not active neurons. Active neurons are represented by 1 and not active by 0
    """

    new_A = []

    # Loop through the activation levels
    for a in A:
        if a < threshold:
            new_A.append(0)
        else:
            new_A.append(1)
    
    return new_A


w = 0.1
I = [1,1,1,1,1,0,0,0,0,0]

print(activation_level(I,w))
A = activation_level(I,w)
print(set_threshold(activation_level(I,w),0.9))

plt.plot(I)
plt.plot([1,2,3,4,5,6,7,8],A)
plt.legend(["Input fra fotoreceptor","Aktiveringsniveau"])
plt.show()