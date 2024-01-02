from rest_framework import viewsets
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication



# Create your views here.

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        user = request.user
        if user.is_superuser == False:
            return Response({"message": "You don't have permission to delete this object"}, status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)