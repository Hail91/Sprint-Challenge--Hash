def has_negatives(a):
    pos_result = []
    neg_result = []
    results = []
    storage = dict()
    for i in range(len(a)):
        storage[i] = a[i]
        if storage[i] > 0:
            positives = storage[i]
            pos_result.append(positives)
        if storage[i] < 0:
            negatives = storage[i]
            neg_result.append(negatives)
    for n in neg_result:
        for p in pos_result:
            if abs(n) == p:
                results.append(p)
    return results

    # If the negative numbers plus the positive number equals zero, then the positive number must have an inverse of itself


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
