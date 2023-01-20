from django import forms

class SubscribeForm(forms.Form):
    email = forms.CharField(label="", max_length=100)
class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50,
                                label="",
                                widget=forms.TextInput(attrs={'placeholder':'Name','class':'form-control input-lg'})
    )
	subject = forms.CharField(max_length = 50,
                                    label="",
                                    widget=forms.TextInput(attrs={'placeholder':'Subject','class':'form-control input-lg'})
    )
	email = forms.EmailField(max_length = 150,
                                    label="",
                                    widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control input-lg'})
    )
	message = forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Email','class':'form-control input-lg'}), max_length = 2000,
    label="",
    )