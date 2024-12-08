def make_validator():
    checks = []

    def add_check(check):
        checks[:] = [check]

    def is_valid(data):
        return all(predicate(data) for predicate in checks)

    return add_check, is_valid