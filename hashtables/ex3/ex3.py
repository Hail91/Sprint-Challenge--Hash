def intersection(arrays):
    storage = dict()
    results = []
    count = 0
    for index, arr in enumerate(arrays):
        for v in arr:
            if storage.get(v) is not None and index > 0:
                storage[v] += 1
            elif storage.get(v) is None and index == 0:
                storage[v] = 1
            else:
                continue
    for values in storage:
        if storage[values] == len(arrays):
            results.append(values)
    return results

intersection([[1, 3, 4], [1, 5, 7], [1, 2, 8]])
            #  x->x->x 

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000,2000000)) + [1,2,3])
#     arrays.append(list(range(2000000,3000000)) + [1,2,3])
#     arrays.append(list(range(3000000,4000000)) + [1,2,3])

#     print(intersection(arrays))
