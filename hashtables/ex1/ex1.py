def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    if limit < 0 or len(weights) < 2 or length < 2:
        return None

    weightsDict = {}
    for index in range(length):
        weightsDict[weights[index]] = index

    i = 0
    for weight in weights:
        if weightsDict.get(limit - weight):
            return (weightsDict.get(limit - weight), i)
        i += 1

# weights_2 = [4, 4]
# answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# print('asn2',answer_2)
# weights_3 = [4, 6, 10, 15, 16]
# answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
# print(answer_3)

# weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
# print(answer_4)