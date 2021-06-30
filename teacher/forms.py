from django import forms


class CourseForm(forms.Form):
    title = forms.CharField(label='Course Title', max_length=30,strip=True)
    subject = forms.CharField(label='Subject Name', max_length=30,strip=True)

class ExamForm(forms.Form):
    title = forms.CharField(label='Exam Title',max_length=30,strip=True)
    description = forms.CharField(label='Exam Description',max_length=50,strip=True)