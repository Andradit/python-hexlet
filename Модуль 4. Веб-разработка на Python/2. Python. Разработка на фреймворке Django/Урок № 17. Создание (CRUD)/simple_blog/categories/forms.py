from django import forms
from simple_blog.categories.models import Category


# BEGIN (write your solution here)
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=200, required=True)
    class Meta:
        model = Category
        fields = ["name", "description", "state"]
# END

'SOLUTION'

'IDENTICAL!!!'