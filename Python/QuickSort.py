def quick_sort(array: list):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    # lessThanPivot = []
    # for x in array:
    #     if x < pivot:
    #         lessThanPivot.append(x)

    lessThanPivot = [x for x in array if x < pivot]
    equalToPivot = [x for x in array if x == pivot]
    greaterThanPivot = [x for x in array if x > pivot]

    return quick_sort(lessThanPivot) + equalToPivot + quick_sort(greaterThanPivot)
