def index_of(coll, value, from_index=0):
    length = len(coll)

    if length == 0:
        return None

    try:
        return coll.index(value, from_index)
    except ValueError:
        return -1