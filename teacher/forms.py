from django import forms


class CourseForm(forms.Form):
    title = forms.CharField(label='Course Title', max_length=30)
    subject = forms.CharField(label='Subject Name', max_length=30)

class ExamForm(forms.Form):
    title = forms.CharField(label='Exam Title',max_length=30)
    description = forms.CharField(label='Exam Description',max_length=50)