def index_of(coll, value, from_index=0):

    if from_index < 0:
        if from_index < -len(coll):
            return []

    try:
        return coll.index(value, from_index)
    except ValueError:
        return -1