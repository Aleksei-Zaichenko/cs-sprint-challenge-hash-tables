def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dictNumber = {}

    for array in arrays:
        print(array)

    print(dictNumber)

    return result


if __name__ == "__main__":
    arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    arrays = [[1,2,3],[1,4,5],[1,6,7]]

    print(intersection(arrays))
