from django import forms
from .models import dab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import CheckboxSelectMultiple

class DabModelForm(forms.ModelForm):
    
    class Meta:
        model = dab
        fields = '__all__'
    
    # def __init__(self, *args, **kwargs):
    #     super(TrickModelForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-trickModelForm'
    #     self.helper.form_class = 'form-group'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'tricks:list'
    #     self.helper.helper.add_input(Submit('submit', 'Submit'))

    # def clean_content(self, *args, **kwargs):
    #     content = self.cleaned_data.get("content")
    #     if content == "abc":
    #         raise forms.ValidationError("Cannot be ABC")
    #     return content