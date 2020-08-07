# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    if len(files) < 0 or len(queries) < 0:
        return []

    result = []
    dictFiles = {}
    dictForFilesThatOccurMore = {}

    for ffile in files:
        temp = ffile.split('/')
        if temp[len(temp) - 1] not in dictFiles:
            dictFiles[temp[len(temp) - 1]] = ffile
        else:
            dictForFilesThatOccurMore[temp[len(temp) - 1]] = ffile
    for query in queries:
        if dictFiles.get(query):
            result.append(dictFiles.get(query))
        if dictForFilesThatOccurMore.get(query):
            result.append(dictForFilesThatOccurMore.get(query))
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/dir256/dirb256/file256',
        '/dir256/file256'
    ]
    queries = [
        "foo",
        "qux",
        "baz",
        "file3490",
        "file256"
    ]
    print(finder(files, queries))
