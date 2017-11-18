from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework import status
from newapi.models import TextUpload
from newapi.serializers import TextUploadSerializer

class getText(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='newapi/gettext.html'
    def get(self, request, *args, **kwargs):
        texts = TextUpload.objects.all()
        serializer = TextUploadSerializer(texts, many=True, read_only=True)
        content = JSONRenderer().render(serializer.data)
        return Response({'content':content})

class uploadText(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='newapi/uploadtext.html'
    def get(self, request, *args, **kwargs):
        serializer =  TextUploadSerializer({'text':'Enter text'})
        return Response({'serializer':serializer})
    def post(self, request, *args, **kwargs):
        serializer =  TextUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer':serializer})
