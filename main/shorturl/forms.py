from django import forms


class MakeForm(forms.Form):
    name = forms.CharField(label='Исходная ссылка')

# class MainForm(forms.Form):
#     tmp = None
