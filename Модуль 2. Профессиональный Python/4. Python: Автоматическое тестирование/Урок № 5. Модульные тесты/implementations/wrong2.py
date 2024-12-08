def make_validator():
    checks = []

    def add_check(check):
        checks.append(check)

    def is_valid(data):
        return False

    return add_check, is_valid