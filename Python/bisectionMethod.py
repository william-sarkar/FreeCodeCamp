def square_root_bisection(number, tolerance=1e-10, iterations=100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    low, high = (0, 1) if number < 1 else (0, number)
    
    for i in range(iterations):
        mid = (low + high) / 2
        square = mid * mid

        if (high - low) <= tolerance:
            print(f"The square root of {number} is approximately {mid}")
            return mid
            
        if square < number:
            low = mid
        else:
            high = mid
            
    print(f"Failed to converge within {iterations} iterations")
    return None
