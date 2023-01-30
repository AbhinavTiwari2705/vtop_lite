from django import forms


class Studentform(forms.Form) :
    s_name=forms.CharField(max_length=100)
    s_current_sem=forms.CharField(max_length=100)
    s_address=forms.CharField(max_length=100)
    s_branch=forms.CharField(max_length=100)
    s_email=forms.EmailField(max_length=100)

class Searchstudentform(forms.Form) :
    s_name=forms.CharField(max_length=100)