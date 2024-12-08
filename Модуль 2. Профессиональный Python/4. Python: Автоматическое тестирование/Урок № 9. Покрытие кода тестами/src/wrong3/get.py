def get(coll, index, default=None):

    if default is not None:
        return default

    if (index >= len(coll) or index < 0):
        return default

    return coll[index]