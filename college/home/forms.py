from django import forms


class Studentform(forms.Form) :
    s_name=forms.CharField(max_length=100,label='Student name')
    s_current_sem=forms.CharField(max_length=100,label='Current Semester')
    s_address=forms.CharField(max_length=100,label='Address')
    s_branch=forms.CharField(max_length=100,label='Branch')
    s_email=forms.EmailField(max_length=100,label='E-mail')

class Droupout(forms.Form) :
    s_name=forms.CharField(max_length=100,label='Student name')
    s_email=forms.EmailField(max_length=100,label='E-mail')