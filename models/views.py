from django.http import Http404
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,
                                                'username': username,
                                                'password': password}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class ServiceListView(APIView):
    def get(self, request, format=None):
        service = Service_Model.objects.all()
        serializer = Service_Serializer(service, many=True)
        return Response(serializer.data)

class ContactCreateView(APIView):
    def post(self, request, format=None):
        serializer = Contact_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CalledContactView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        called = Contact_Model.objects.filter(called="Bog'lanildi")
        serializer = Contact_Serializer(called, many=True)
        return Response(serializer.data)

class UnCalledContactView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        called = Contact_Model.objects.filter(called="Bog'lanilmadi")
        serializer = Contact_Serializer(called, many=True)
        return Response(serializer.data)

class AllContactView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        service = Contact_Model.objects.all()
        serializer = Contact_Serializer(service, many=True)
        return Response(serializer.data)

class ContactDetailView(APIView):
    """
    Retrieve, update or delete a transformer instance
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Contact_Model.objects.get(pk=pk)
        except Contact_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
            conatct = self.get_object(pk)
            serializer = Contact_Serializer(conatct,
                                               data=request.data,
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            conatct = self.get_object(pk)
            conatct.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




class ServiceCreateView(APIView):
    def post(self, request, format=None):
        serializer = Service_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceDetailView(APIView):
    """
    Retrieve, update or delete a transformer instance
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Service_Model.objects.get(pk=pk)
        except Service_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            service = self.get_object(pk)
            serializer = Service_Serializer(service)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
            service = self.get_object(pk)
            serializer = Service_Serializer(service, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
            service = self.get_object(pk)
            serializer = Service_Serializer(service,
                                               data=request.data,
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            service = self.get_object(pk)
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)





class ServiceSectionListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        service = Service_Section_Model.objects.all()
        serializer = Service_Sections_Serializer(service, many=True)
        return Response(serializer.data)

class ServiceSectionCreateView(APIView):
    def post(self, request, format=None):
        serializer = Service_Sections_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceSectionDetailView(APIView):
    """
    Retrieve, update or delete a transformer instance
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Service_Section_Model.objects.get(pk=pk)
        except Service_Section_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            service = self.get_object(pk)
            serializer = Service_Sections_Serializer(service)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
            service = self.get_object(pk)
            serializer = Service_Sections_Serializer(service, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
            service = self.get_object(pk)
            serializer = Service_Sections_Serializer(service,
                                               data=request.data,
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            service = self.get_object(pk)
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)