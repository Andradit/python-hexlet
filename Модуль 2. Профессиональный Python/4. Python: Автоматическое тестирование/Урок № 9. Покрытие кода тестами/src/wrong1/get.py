def get(coll, index, default=None):

    if (index >= len(coll) or index < 0):
        if default is not None:
            return False
        return None

    return coll[index]