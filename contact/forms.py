from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField()
	your_email = forms.EmailField(required=True)
	message = forms.CharField(widget=forms.Textarea , required=True)
