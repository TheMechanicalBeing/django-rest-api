from django import forms

from .models import Block, Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

    def clean(self):
        cleaned_data = super(MenuForm, self).clean()
        link = cleaned_data.get('link')
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')

        if not category:
            if not link or not name:
                raise forms.ValidationError('You should enter either category or link and name')

        return cleaned_data


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        exclude = ('articles',)
