from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  UserSerializer


class UserAPIView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        