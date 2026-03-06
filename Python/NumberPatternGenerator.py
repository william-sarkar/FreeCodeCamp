def number_pattern(n):
    result = []
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    
    for num in range(1, n+1):
        result.append(str(num))
    
    resultString = ' '.join(result)
    return resultString
