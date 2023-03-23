from rest_framework import serializers

class HelloSerialzer(serializers.Serializer):
    """Serializer a name field for testing APIView"""
    name=serializers.CharField(max_length=10)
