from django import forms
from .models import Print, Category


class PrintForm(forms.ModelForm):

    class Meta:
        model = Print
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        names = [(c.id, c.name) for c in categories]

        self.fields['category'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'