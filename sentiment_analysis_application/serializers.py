from rest_framework import serializers


class SentimentAnalysisSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=200)
