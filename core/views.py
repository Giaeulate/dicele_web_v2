from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FormField
from .serializers import FormFieldSerializer


class FormFieldList(APIView):
    def get(self, request):
        fields = FormField.objects.all()
        serializer = FormFieldSerializer(fields, many=True)
        return Response(serializer.data)
