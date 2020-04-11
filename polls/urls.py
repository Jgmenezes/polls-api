from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Polls API')

from .apiviews import PollListCreate, \
    PollDetail, \
    ChoiceListCreate, \
    CreateVote, \
    UserCreate, \
    LoginView

urlpatterns = [
    path("polls/", PollListCreate.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceListCreate.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="Login"),
    path(r'swagger-docs/', schema_view)
]
