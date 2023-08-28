from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import competition_get, vote, singer_get
from .serializers import VoteSerializer, VoteResultSerializer
from .models import Vote

class VoteAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VoteSerializer

    def post(self, request, competition_id):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        competition = competition_get(competition_id=competition_id)
        singer = singer_get(singer_name=serializer.validated_data["singer_name"])

        vote(user=request.user, competition=competition, singer=singer)

        return Response("user voted successfully", status=status.HTTP_201_CREATED)
    

class ViewCurrentResult(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = VoteResultSerializer

    def get(self, request, competition_id):
        competition = competition_get(competition_id=competition_id)
        
        if not Vote.objects.filter(competition=competition, voter=request.user).exists():
            return Response("You have not voted for this competition", status=status.HTTP_400_BAD_REQUEST)

        serializer = VoteResultSerializer(competition)
        return Response(serializer.data)