from django.urls import path
from .views import FormFieldList

urlpatterns = [
    path('api/fields/', FormFieldList.as_view(), name='form-field-list'),
]
