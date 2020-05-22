def finder(files, queries):
    storage = dict()
    result = []

    for q in queries:
        # Loop over Queries and add them to dictionary as lists
        storage[q] = []
    # Loop over files tracking the index and file
    for i, file in enumerate(files):
        # split the file only paying attention to the last string after the forward slash
        f = file.split('/')[-1]
        # If the file exists in the dictionary, then append it to result array and return that
        if f in storage.keys():
            result.append(file)
    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
