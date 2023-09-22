from django.urls import path,include
from .views import PictureView, GetPerson, GetRandomCode, CreatePerson, PersonUpdateRating
from .views import GetToken
urlpatterns = [
    path('persons',PictureView.as_view()),
    path('get_person',GetPerson.as_view()),
    path('get_two_random_codes',GetRandomCode.as_view()),
    path('create_person',CreatePerson.as_view()),
    path('update_rating',PersonUpdateRating.as_view()),
    path('get_token',GetToken.as_view())
]