from .models import *
from rest_framework import serializers



class DocumentSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField("get_url")

    class Meta:
        model = Document
        fields = ('url', 'date_creation','nom','typeFile')

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.document.url)





    # def validate(self, data):
    #     document = Document()
    #     if document:
    #         return document
    #     raise serializers.ValidationError("Invalid Details.")


