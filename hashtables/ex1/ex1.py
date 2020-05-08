def get_indices_of_item_weights(weights, length, limit):
    storage = dict()
    # Loop over the weights list, and assign each value to a key in storage dictionary
    for v in range(length):
        x = storage.get(limit - weights[v])
        print(x)
        if x is not None:
            print(v, x)
            return (v, x)
        else:
            storage[weights[v]] = v
    return None
weights_3 = [4, 6, 10, 15, 16]
get_indices_of_item_weights(weights_3, 5, 21)
