from rest_framework import serializers
from .models import Competition

class VoteSerializer(serializers.Serializer):
    singer_name = serializers.CharField()


class VoteResultSerializer(serializers.ModelSerializer):
    singer_a_votes = serializers.IntegerField()
    singer_b_votes = serializers.IntegerField()

    class Meta:
        model = Competition
        fields = ['singer_a_votes', 'singer_b_votes']

    def get_singer_a_votes(self, obj):
        return obj.singer_a_votes
    
    def get_singer_b_votes(self, obj):
        return obj.singer_b_votes
    