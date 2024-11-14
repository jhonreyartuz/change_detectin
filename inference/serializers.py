# serializers.py
from rest_framework import serializers

class InferenceResultSerializer(serializers.Serializer):
    model = serializers.FileField()
    weight = serializers.FileField()
    before_image = serializers.ImageField()
    after_image = serializers.ImageField()
