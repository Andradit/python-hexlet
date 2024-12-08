def my_slice(coll, start=0, end=None):
    length = len(coll)

    normalized_end = length if end is None else end

    if start < 0:
        if start >= -length:
            return coll[1:]

    return coll[start:normalized_end]
