from django import forms


class CourseForm(forms.Form):
    title = forms.CharField(label='Course Title', max_length=30)
    subject = forms.CharField(label='Subject Name', max_length=30)
