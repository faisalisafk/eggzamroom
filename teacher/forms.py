from django import forms


class CourseForm(forms.Form):
    title = forms.CharField(label='Course Title', max_length=30)
    subject = forms.CharField(label='Subject Name', max_length=30)

class EditProfileForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=200)
    lastName = forms.CharField(label='Last Name', max_length=200)
    email = forms.EmailField(label='Email', max_length=60)