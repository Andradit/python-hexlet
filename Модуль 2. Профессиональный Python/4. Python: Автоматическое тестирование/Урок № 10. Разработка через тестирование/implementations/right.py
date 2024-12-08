def fill(coll, value, begin=0, end=None):
    chunk = [value for _ in coll[begin:end]]
    coll[begin:end] = chunk