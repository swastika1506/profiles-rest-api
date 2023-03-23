from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """return a list of view features"""
        an_apiview=[
        'Uses HTTP method as function(get,post, patch,put,delete)',
        'is similar to a traditional django view',
        'gives you the most control over your app logic',
        'is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!','an_apiview': an_apiview})
