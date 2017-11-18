from rest_framework import serializers
from newapi.models import TextUpload

class TextUploadSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length = 1000)
    class Meta:
        model = TextUpload
        fields = ('id', 'text')
