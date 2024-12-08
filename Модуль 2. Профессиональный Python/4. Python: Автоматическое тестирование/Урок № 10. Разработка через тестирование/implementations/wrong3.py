def fill(coll, value, begin=0, end=None):
    coll_length = len(coll)
    if not end:
        end = coll_length
    i = begin
    while i < end:
        coll[i] = value
        i += 1