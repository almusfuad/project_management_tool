from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.contrib.auth.models import User 



class UsersViewset(viewsets.ModelViewSet):
      queryset = User.objects.all() 
      serializer_class = UserSerializer
      permission_classes = [IsAuthenticated]

      def post(self, request, *args, **kwargs):
            self.permission_classes = [IsAdminUser]   # only admin can create user
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data, status = status.HTTP_201_CREATED)                
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
