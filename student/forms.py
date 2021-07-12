from django import forms


class CourseJoinForm(forms.Form):
    courseCode = forms.CharField(label='Course Code', max_length=30,strip=True)


