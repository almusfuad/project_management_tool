from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import UserSerializer



class UsersViewset(viewsets.ModelViewSet):
      """
      A viewset for managing users registration, login, and details.
      Endpoints:
            - POST /api/users/register: Register a new user.
            - POST /api/users/login: Login an existing user.
            - GET /api/users/{id}: Retrieve user details.
            - PUT/PATCH /api/users/{id}: Update user details.
            - DELETE /api/users/{id}: Delete a user.

      """
      queryset = User.objects.all() 
      serializer_class = UserSerializer


      @action(detail=False, methods=["POST"], url_path="register")
      def register(self, request):
            """Handle user registration."""
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
      

      @action(detail=False, methods=["POST"], url_path="login")
      def login(self, request):
            """Handle user login and return JWT token."""
            username = request.data.get("username")
            password = request.data.get("password")

            try:
                  user = User.objects.get(username=username)
                  if user.check_password(password):
                        # Generate new JWT token
                        refresh = RefreshToken.for_user(user)
                        return Response({
                              "refresh": str(refresh),
                              "access": str(refresh.access_token)
                        }, status=200)
                  else:
                        return Response({"error": "Invalid credentials"}, status=400)
            except User.DoesNotExist:
                  return Response({"error": "User not found"}, status=404)
            


