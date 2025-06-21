# BEGIN (write your solution here)
def validate(value):
    errors = {}
    if not value['title']:
        errors['title'] = "Can't be blank"
    if not value['paid']:
        errors['paid'] = "Can't be blank"
    return errors
# END

'SOLUTION'

# def validate(course):
#     errors = {}
#     if not course.get('title'):
#         errors['title'] = "Can't be blank"
#     if not course.get('paid'):
#         errors['paid'] = "Can't be blank"
#     return errors