from django.urls import path
from . import views

urlpatterns = [
    path("competition/<int:competition_id>/vote/", views.VoteAPIView.as_view(), name="vote"),
    path("competition/<int:competition_id>/result/", views.ViewCurrentResult.as_view(), name="result"),
]