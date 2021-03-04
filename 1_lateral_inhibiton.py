def activation_level(I,w):
    """ Calculate activation levels

    Args:
        I (list): Inputs from photoreceptor
        w (int): Weight of lateral inhibition

    Returns:
        List: Activiation levels of each element
    """
    
    A = []
    for index, level in enumerate(I):
        # print(index)
        if index == 0:
            a = level - I[index+1]*w
            A.append(a)
        elif index == len(I)-1:
            a = level - I[index-1]*w
            A.append(a)
        else:
            a = I[index] - w*(I[index-1]+I[index+1])
            A.append(a)
    return A

w = 0.1
I = [1,1,1,1,1,0,0,0,0,0]

print(activation_level(I,w))
