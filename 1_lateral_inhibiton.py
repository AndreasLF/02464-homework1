def activation_level(I,w):
    """ Calculate activation levels. 
    
    The activation of the two cells at the endpoints are ignored.

    Args:
        I (list): Inputs from photoreceptor
        w (int): Weight of lateral inhibition

    Returns:
        List: Activiation levels of each element
    """
    
    A = []
    
    for index, _ in enumerate(I):
        # If it is not the first and not the last element in the list
        if index != 0 and index != len(I)-1:
            # Calculate the activation level
            a = I[index] - w*(I[index-1]+I[index+1])
            A.append(a)
    return A

w = 0.1
I = [1,1,1,1,1,0,0,0,0,0]

print(activation_level(I,w))
