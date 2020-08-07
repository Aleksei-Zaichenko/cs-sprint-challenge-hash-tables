def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    posNumber = {}
    negNUmber = {}
    for number in a:
        if number > 0:
            posNumber[number] = number
        else:
            negNUmber[number] = number

    for number in posNumber.keys():
        if negNUmber.get(number * (-1)):
            result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
