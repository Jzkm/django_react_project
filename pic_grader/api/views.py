from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random
from .serializers import PersonCreateSerializer, PersonUpdateRatingSerializer
from .evaluate_rank import evaluate_rank
from django.middleware.csrf import get_token
# from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from .jan_security import HasAPIKey



class GetToken(APIView):
    permission_classes = [HasAPIKey]
    @staticmethod
    def get(request,format = None):
        # Pobierz token CSRF
        csrf_token = get_token(request)

        # Przekształć token na JSON lub inny format
        response_data = {'csrf_token': csrf_token}

        # Zwróć odpowiedź JSON z tokenem CSRF
        return JsonResponse(response_data)

class PictureView(generics.ListAPIView):
    # permission_classes = [HasAPIKey]
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class GetPerson(APIView):
    permission_classes = [HasAPIKey]
    serializer_class = PersonSerializer
    lookup_url_kwarg = 'pcode'

    def get(self,request,format = None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            person = Person.objects.filter(code=code)
            if len(person) > 0:
                data = PersonSerializer(person[0]).data
                return Response(data,status=status.HTTP_200_OK)
            return Response("Person not found",status=status.HTTP_404_NOT_FOUND)
        return Response("Enter person code",status=status.HTTP_400_BAD_REQUEST)
    
class GetRandomCode(APIView):
    permission_classes = [HasAPIKey]
    serializer_class = PersonSerializer
    def get(self,format = None):
        persons = Person.objects.all()
        los1 = random.choice(persons)
        los1 = los1.code
        los2 = los1
        while los2 == los1:
            los2 = random.choice(persons)
            los2 = los2.code
        data = f"{los1}{los2}"
        # data.append()
        # data = PersonSerializer(random.choice(persons)).data
        return Response(data,status=status.HTTP_200_OK)
    

class CreatePerson(generics.CreateAPIView):
    permission_classes = [HasAPIKey]
    queryset = Person.objects.all()
    serializer_class = PersonCreateSerializer


class PersonUpdateRating(generics.CreateAPIView):
    permission_classes = [HasAPIKey]
    serializer_class = PersonUpdateRatingSerializer
    # permission_classes = [IsAuthenticated]


    def post(self,request,format=None):
        serializer = self.serializer_class(data=request.data)
        #print(request.data)
        if serializer.is_valid():
            code = serializer.data.get('code')
            enymycode = serializer.data.get('enymycode')
            rank = serializer.data.get('rank')
            enymyrank = serializer.data.get('enymyrank')
            queryset = Person.objects.filter(code=code)
            if queryset.exists():
                person = queryset[0]
                # print(person.rank)
                person.rank = evaluate_rank(rank,enymyrank,True)
                # print(person.rank)
                # print(person.plec)
                # print(person.code)
                person.save(update_fields=['rank'])
            #     return Response(PersonSerializer(person).data, status=status.HTTP_200_OK)
            else:
                return Response({'Person not found'}, status=status.HTTP_404_NOT_FOUND)
            
            queryset = Person.objects.filter(code=enymycode)
            if queryset.exists():
                person = queryset[0]

                person.rank = evaluate_rank(enymyrank,rank,False)
                person.save(update_fields=['rank'])
                return Response(PersonSerializer(person).data, status=status.HTTP_200_OK)
            else:
                return Response({'Person not found'}, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({'Bad serializer'}, status=status.HTTP_400_BAD_REQUEST)
            
                
            



    
        
             




