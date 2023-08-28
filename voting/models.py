from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Singer(models.Model):
    name = models.CharField(max_length=50)


class Competition(models.Model):
    singer_a = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="singer_a_competition")
    singer_b = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="singer_b_competition")

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self) -> str:
        return self.singer_a.name + " | " + self.singer_b.name
    
    @property
    def singer_a_votes(self):
        return self.competition_votes.filter(vote_for=self.singer_a).count()

    @property
    def singer_b_votes(self):
        return self.competition_votes.filter(vote_for=self.singer_b).count()
    

class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_votes")

    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, related_name="competition_votes")
    vote_for = models.ForeignKey(Singer, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user.email