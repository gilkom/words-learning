from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from nauka.models import Word, Learning, User
from nauka.serializers import * #WordSerializer, LearningSerializer, UserSerializer, UserRegistrationSerializer
from . import serializers
from django.db import connection
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication


# Create your views here.

        
class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes=[IsAdminUser]

    

class UserWordsViewSet(viewsets.ModelViewSet):
    serializer_class = WordSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.headers.get('x-user')
        #Dla api svelte jest x-user
        if user is None:
            user = self.request.user
        return Word.objects.filter(owner=user)


class WordToLearnViewSet(viewsets.ViewSet):
    serializer_class = WordSerializer

    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT w.*
                FROM nauka_word w
                LEFT JOIN nauka_learning l
                ON w.word_id = l.word_id_id
                WHERE l.word_id_id IS NULL
                AND w.owner_id = %s
            ''', [request.user.id])
            rows = cursor.fetchall()

        words_to_learn = [Word.objects.get(pk=row[0]) for row in rows]

        serializer = self.serializer_class(words_to_learn, many=True)
        return Response(serializer.data)
    


class LearningViewSet(viewsets.ModelViewSet):
    queryset = Learning.objects.all()
    serializer_class = LearningSerializer
    permission_classes=[IsAdminUser]

class UserLearningViewSet(viewsets.ViewSet):
    serializer_class = LearningSerializer

    def list(self, request):
        with connection.cursor() as cursor:
            cursor.execute('''
                    SELECT l.*
                    FROM nauka_learning l
                    WHERE l.owner_id = %s
                           ''', [request.user.id])
            rows = cursor.fetchall()
        user_learnings = [Learning.objects.get(pk=row[0]) for row in rows]

        serializer = self.serializer_class(user_learnings, many=True)
        return Response(serializer.data)
    
  
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class RegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    model = User
    permission_classes = [AllowAny]


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_id = serializer.validated_data['user_id']
        login(request, user)
        return Response({'username':user.username, 'id':user_id}, status=status.HTTP_202_ACCEPTED)

class LogoutView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    #@login_required
    def post(self, request, format=None):
        logout(request)
        request.session.clear()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
    
    '''def get(self, request, format=None):
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
    '''
'''
@api_view(['GET'])
def check_login_status(request):
    if request.user.is_authenticated:
        user = {
            'username': request.user.username,
            'password': request.user.password,
            # inne informacje o użytkowniku
        }
        return JsonResponse({'user': user})
    else:
        return Response({'error': 'Unauthorized'}, status=401)
        '''