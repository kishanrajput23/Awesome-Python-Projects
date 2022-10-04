import django_filters
from django_filters import DateFilter
from django import forms

from .models import *


class UniversityFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields = '__all__'
        exclude = ['university_id', 'Website']

class universityInfoFilter(django_filters.FilterSet):

    univ_name = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = University_Info
        fields = ['univ_name']
