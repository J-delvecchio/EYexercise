
    
C = [0,1,0,0,0,1,0] # the size must be in the range [2,100], must be filled with just 0,1 and the first and last elements must be 0

def jumpOnMarsh(C):
    
    """
    Summary:
    Function that takes an array filled with binary digit, which is a path with 0 as stones/safe and 1 as pit/avoid, and returns the minimum numbers of jumps requiered to get across it.

    Args:
      array: C , filled with binary digits (0,1)

    Returns:
        int: cont, minimum number of jumps requiered
    """
    
    #If the size of the array is minor or equal to 3 then there is no need to enter the while, I just return 1 as the minimun number of jumps required
    
    if len(C) <=3:                           
        return 1
    
    i = 0
    cont = 0
    while i < len(C)-1:
        # Condition to not get out of range
        if i < len(C)-2 and C[i+2] == 0:           
            i+=2
        else:
            i+=1
        cont+=1                
    return cont
    
    
print(jumpOnMarsh(C))
