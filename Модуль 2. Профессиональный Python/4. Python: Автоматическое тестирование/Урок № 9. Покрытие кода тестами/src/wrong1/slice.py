def my_slice(coll, start=0, end=None):
    length = len(coll)

    normalized_end = length if end is None else end

    if length == 0:
        return None

    return coll[start:normalized_end]
