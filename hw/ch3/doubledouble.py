def doubledouble(sequence):
    result = []
    for element in sequence:
        double = str(element * 2)
        result = result + [double + double]
    return result


